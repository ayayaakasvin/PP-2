def find_lowercase_with_underscore(s : str):
    import re

    subRE = r"[a-z]+_[a-z]+"

    if re.match(subRE, s):
        return "Match Found"
    else:
        return "Not Found"
    
print(find_lowercase_with_underscore("ashdbcnliscn_aijsndmaksjc "))
print(find_lowercase_with_underscore("as_"))
print(find_lowercase_with_underscore("asdasfA_asd"))
print(find_lowercase_with_underscore("_"))