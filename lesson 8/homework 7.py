def calculator_decorator(func):
    def wrapper(expression):
        try:

            result = func(expression)
            return result
        except (SyntaxError, NameError, ZeroDivisionError) as e:

            return f"Error: {e}"
        except Exception as e:

            return f"An unexpected error occurred: {e}"

    return wrapper


@calculator_decorator
def calculate(expression):
    return eval(expression)


if __name__ == "__main__":
    while True:

        user_input = input("Enter a mathematical expression (or type 'exit' to quit): ")

        if user_input.lower() == 'exit':
            break


        result = calculate(user_input)
        print(f"Result: {result}")