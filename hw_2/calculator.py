# Prompt to input numbers
number_1 = float(input('Enter the first number: '))
number_2 = float(input('Enter the second number: '))

# Select the operator
operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

# Counting
if operation == '+':
    print("The result is: ", (number_1 + number_2))

elif operation == '-':
    print("The result is: ", (number_1 - number_2))

elif operation == '*':
    print("The result is: ", (number_1 * number_2))

elif operation == '/':
    if number_2 != 0:
        print("The result is: ", (number_1 / number_2))
    else:
        print("Sorry, cannot divide by 0")

else:
    print('Not a valid operator is entered. Please run the program again.')
