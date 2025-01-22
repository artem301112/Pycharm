import random

class Encryption:
    def __init__(self, *numbers):
        self.numbers = numbers
        self.result = self._encrypt()

    def _encrypt(self):
        operations = [self._add, self._subtract, self._multiply, self._divide]
        operation = random.choice(operations)
        return operation()

    def _add(self):
        return sum(self.numbers)

    def _subtract(self):
        result = self.numbers[0]
        for number in self.numbers[1:]:
            result -= number
        return result

    def _multiply(self):
        result = 1
        for number in self.numbers:
            result *= number
        return result

    def _divide(self):
        result = self.numbers[0]
        try:
            for number in self.numbers[1:]:
                result /= number
        except ZeroDivisionError:
            return "Division by zero error"
        return result

    def __repr__(self):
        return f"Result of encryption: {self.result}"

enc = Encryption(10, 5, 2)
print(enc)