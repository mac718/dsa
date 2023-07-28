from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder( root: Optional[TreeNode]) -> List[List[int]]:
    def getHeight(node):
        if not node:
            return 0
        return max(1 + getHeight(node.left), 1 + getHeight(node.right))

    height = getHeight(root)
    res = [[] for i in range(height)]
    q = [(root, 0)]
    visited = set()
    while len(q):
        cur = q.pop(0)
        if cur in visited:
            continue

        visited.add(cur)

        if cur[0]:
            res[cur[1]].append(cur[0].val)
        if cur[0]:
            q.append((cur[0].left, cur[1] + 1))
            q.append((cur[0].right, cur[1] + 1))

    return res

