def a_followed_by_anything_and_b(s : str):
    import re

    subRE = r"a.*b$"

    if re.match(subRE, s):
        return "Match Found"
    else:
        return "Not Found"
    
print(a_followed_by_anything_and_b("adaokfmapsdb"))
print(a_followed_by_anything_and_b("ab"))
print(a_followed_by_anything_and_b("aasdbbab"))
print(a_followed_by_anything_and_b("aasdba"))
