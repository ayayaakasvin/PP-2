def find_uppercase_with_lowercase(s : str):
    import re

    subRE = r"[A-Z][a-z]+"

    if re.match(subRE, s):
        return "Match Found"
    else:
        return "Not Found"
    
print(find_uppercase_with_lowercase("Aida"))
print(find_uppercase_with_lowercase("Jokerge"))
print(find_uppercase_with_lowercase("Gayge"))
print(find_uppercase_with_lowercase("aSa"))