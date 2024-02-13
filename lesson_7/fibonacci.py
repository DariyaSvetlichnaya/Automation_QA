def fibonacci(n):
    if n <= 0:
        print("The number should be more than 0")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(fibonacci(1))
    print(fibonacci(5))
    print(fibonacci(10))
    print(fibonacci(15))
    print(fibonacci(20))
    print(fibonacci(30))
