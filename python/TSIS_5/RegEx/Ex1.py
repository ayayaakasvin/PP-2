def find_ab_in_RE(s : str) -> str:
    import re

    subRE = r"ab*"

    if re.match(subRE, s):
        return "Match found"
    else:
        return "Not found"
    
print(find_ab_in_RE("a"))
print(find_ab_in_RE("ab"))
print(find_ab_in_RE("abb"))
print(find_ab_in_RE("abbbbb"))
print(find_ab_in_RE("abbbbbbbbbbb"))
print(find_ab_in_RE("aab"))
print(find_ab_in_RE("aabababa"))
print(find_ab_in_RE("b"))