def lengthOfLongestSubstring(s: str) -> int:
    l = 0
    max_sub = 0
    sub_set = set()
    for r in range(len(s)):
        while s[r] in sub_set:
            sub_set.remove(s[l])
            l += 1
        sub_set.add(s[r])
        max_sub = max(max_sub, r - l + 1)

    return max_sub