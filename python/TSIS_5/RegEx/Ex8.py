def split_by_uppercase (s : str) -> list:
    import re

    return re.findall("[A-Z][^A-Z]*", s)

print(split_by_uppercase("auydbfKapsidjKidL"))