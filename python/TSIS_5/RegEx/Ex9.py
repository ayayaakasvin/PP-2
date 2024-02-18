def add_space_before_capital (s : str) -> str:
    import re

    listOfStrings = re.findall("[A-Z][^A-Z]*", s)
    answer = f"{listOfStrings[0]}"
    for i in listOfStrings[1::]:
        answer += ' ' + i

    return answer

print(add_space_before_capital("AveMarieDeusVult"))w