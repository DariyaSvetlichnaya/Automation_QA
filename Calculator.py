# Prompt to input numbers
number_1 = int(input('Enter the first number: '))
number_2 = int(input('Enter the second number: '))

#Select the operator
operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

#Counting
if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

elif operation == '/':
    if number_2 != 0:
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
    else:
        print("Sorry, cannot divide by 0")

else:
    print('Not a valid operator is entered. Please run the program again.')