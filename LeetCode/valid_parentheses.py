def valid_parentheses(s: str) -> bool:
    if s[0] in ")}]":
        return False
    opposing_pairs = {"}": "{", ")": "(", "]": "["}
    stack = []

    for bracket in s:
        if bracket in opposing_pairs:
            if len(stack) and stack[-1] == opposing_pairs[bracket]:
                stack.pop()
            else:
                return False
        else:
            stack.append(bracket)

    return len(stack) == 0
