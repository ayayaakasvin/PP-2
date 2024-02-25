from functools import reduce

def multiply_list(numbers):
    if not numbers:
        return None
    return reduce(lambda x, y: x * y, numbers)

some_array = [1, 2, 3, 4, 5, 6]
print(multiply_list(some_array))