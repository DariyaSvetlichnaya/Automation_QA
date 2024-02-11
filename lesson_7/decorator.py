def fn_name(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        print(f"Function '{fn.__name__}' is called. Result: {result}")
        return result
    return wrapper


@fn_name
def add(a, b):
    return a + b


@fn_name
def multiply(a, b):
    return a * b


# Example
result_sum = add(5, 5)
result_mult = multiply(4, 6)
