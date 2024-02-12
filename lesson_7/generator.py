def squares():
    for i in range(0, 1000000001, 2):
        yield i ** 2


generator = squares()
for even_squares in generator:
    print(even_squares)
