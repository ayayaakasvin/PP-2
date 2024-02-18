def find_ab_in_string (s : str) -> str:
    import re

    subRE = r"ab{2,3}"

    if re.match(subRE, s):
        return "Match found"
    else:
        return "Not Found"
    

print(find_ab_in_string("ab"))
print(find_ab_in_string("abb"))
print(find_ab_in_string("abbb"))
print(find_ab_in_string("aa"))
print(find_ab_in_string("aaa"))
print(find_ab_in_string("aaaa"))