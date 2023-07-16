def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_char_count = {}
    t_char_count = {}

    for i in range(len(s)):
        if s[i] in s_char_count:
            s_char_count[s[i]] += 1
        else:
            s_char_count[s[i]] = 1
        if t[i] in t_char_count:
            t_char_count[t[i]] += 1
        else:
            t_char_count[t[i]] = 1

    for c in s_char_count:
        if c not in t_char_count or (s_char_count[c] != t_char_count[c]):
            return False

    return True
