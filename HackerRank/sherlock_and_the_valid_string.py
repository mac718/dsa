from collections import Counter

def isValid(s):
    char_count = Counter(s)
    char_count_values = char_count.values()
    char_count_values_count = Counter(char_count_values)

    if len(char_count_values_count.keys()) > 2:
        return "NO"
    if len(char_count_values_count.keys()) == 2:
        values = list(char_count_values_count.values())
        keys = list(char_count_values_count.keys())
        if abs(keys[0] - keys[1]) != 1 and (char_count_values_count[1] != 1):
            return "NO"
        if values[0] != 1 and values[1] != 1:
            return "NO"
    return "YES"