def print_table(num, operation):
    result = 0
    for i in range(1, 11):
        if operation == '+':
            result = num + i
        elif operation == '*':
            result = num * i
        print(f"{num} {operation} {i} = {result}")


def get_sum(num, operation):
    print_table(num, operation)
    result = sum([num + i for i in range(10)])
    return result


if __name__ == '__main__':
    number = int(input("Enter a number: "))
    op = input("Enter an operation (+ or *): ")
    print('Sum is', get_sum(number, op))
