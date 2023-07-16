from typing import List


def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    orig_color = image[sr][sc]
    stack = [(sr, sc)]
    visited = set()
    adjacent = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    while len(stack):
        curr = stack.pop()
        if curr in visited:
            continue
        if image[curr[0]][curr[1]] != orig_color:
            continue
        visited.add(curr)
        if image[curr[0]][curr[1]] == orig_color:
            image[curr[0]][curr[1]] = color
        for dir in adjacent:
            if 0 <= curr[0] + dir[0] <= len(image) - 1 and 0 <= curr[1] + dir[1] <= len(image[0]) - 1:
                sr = curr[0] + dir[0]
                sc = curr[1] + dir[1]

                stack.append((sr, sc))
    return image
