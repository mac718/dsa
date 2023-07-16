import re


def isPalindrome(self, s: str) -> bool:
    alpha_num = re.compile("[0-9a-z]")
    l = 0
    r = len(s) - 1
    while l < r:
        left = s[l].lower()
        right = s[r].lower()
        if alpha_num.search(left) is None:
            l += 1
            continue
        elif alpha_num.search(right) is None:
            r -= 1
            continue
        elif right != left:
            return False
        r -= 1
        l += 1
    return True
