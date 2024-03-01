import time


def count_time(fn):

    def wrapper(*args, **kwargs):
        current_time = time.time()
        result = fn(*args, **kwargs)
        print(f"Result is: {result}")
        print(f"Function executed in: {time.time() - current_time}")
        return result
    return wrapper


@count_time
def add(a, b):
    time.sleep(5)
    return a + b


result_sum = add(500, 700)
