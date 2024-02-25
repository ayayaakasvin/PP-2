def is_pallindrom(some_string : str) -> bool:
    return some_string.lower() == some_string[::-1].lower()

print(is_pallindrom("Amana"))
print(is_pallindrom("Lol"))
