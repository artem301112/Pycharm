import requests
from bs4 import BeautifulSoup

class CurrencyConverter:
    def __init__(self):
        self.url = "https://bank.gov.ua/en/markets/exchangerates"
        self.rates = self.get_rates()

    def get_rates(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            rates = {}
            for currency in ['USD', 'GBP', 'EUR']:
                rate = soup.find('td', string=currency).find_next_sibling('td').text.strip()
                if currency == 'GBP':
                    rates['Pounds'] = float(rate)
                else:
                    rates[currency] = float(rate)
            rates['UAH'] = 1.0  # Adding UAH as its own rate
            return rates
        except requests.RequestException as e:
            print(f"Error fetching exchange rates: {e}")
            return {}
        except AttributeError:
            print("Error parsing exchange rates. The structure of the webpage may have changed.")
            return {}

    def convert_to_usd(self, amount, currency):
        if currency == 'USD':
            return amount  # No conversion needed if already in USD
        if currency in self.rates:
            return amount / self.rates[currency]
        raise ValueError(f"Unsupported currency: {currency}")

def main():
    converter = CurrencyConverter()
    if not converter.rates:
        print("Unable to fetch exchange rates. Please try again later.")
        return

    while True:
        currency = input("Enter the currency (UAH, Pounds, EUR, USD): ").strip().capitalize()
        if currency not in ['UAH', 'Pounds', 'EUR', 'USD']:
            print("Invalid currency. Exiting...")
            break

        try:
            amount = float(input(f"Enter the amount in {currency}: "))
        except ValueError:
            print("Invalid amount. Exiting...")
            break

        try:
            usd_amount = converter.convert_to_usd(amount, currency)
            print(f"The equivalent amount in USD is: {usd_amount:.2f}")
        except ValueError as e:
            print(e)
            break

if __name__ == "__main__":
    main()