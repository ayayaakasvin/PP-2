def number_of_uppercase_letters (some_string : str) -> str:
    if not some_string:
        return "Empty string"
    else:
        from functools import reduce
        uppercase_letters : int = reduce(lambda a, b: a + 1 if b.isupper() else a, some_string, 0)
        lowercase_letters : int = reduce(lambda a, b: a + 1 if b.islower() else a, some_string, 0)
        return f"Number of uppercase letter - {uppercase_letters}, lowercase letters - {lowercase_letters}"
    
print(number_of_uppercase_letters("Some String"))