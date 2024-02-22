class FormulaError(Exception):
    pass


class WrongOperatorError(Exception):
    pass


def calculate(count):
    try:
        # Split the formula into its components
        num1, operator, num2 = count.split()

        # Check if the operator is valid
        if operator not in ('*', '/'):
            raise WrongOperatorError("Invalid operator. Please use '*' or '/'.")

        # Convert the numbers to floats
        num1 = float(num1)
        num2 = float(num2)

        # Perform the calculation based on the operator
        if operator == '*':
            res = num1 * num2
        else:
            # Check for division by zero
            if num2 == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            res = num1 / num2

        # Round the result to two decimal places
        return round(res, 2)

    except ValueError:
        raise FormulaError("Invalid input. Enter 2 numbers with operator '*' or '/' in the middle divided by spaces.")


# Number of attempts allowed
attempts = 3

while attempts > 0:
    try:
        # Prompt the user to enter a formula
        expression = input("Please, enter two numbers with operator '*' or '/' in the middle divided by spaces: ")
        # Calculate the result
        result = calculate(expression)
        # Print the result
        print("Result:", result)
        # Break if calculation is successful
        break
    except FormulaError as e:
        # Handle formula-related errors
        print(e)
        attempts -= 1
    except WrongOperatorError as e:
        # Handle wrong operator errors
        print(e)
        attempts -= 1
    except ZeroDivisionError as e:
        # Handle division by zero errors
        print(e)
        attempts -= 1

# If no attempts left
if attempts == 0:
    print("Attempts are over.")
