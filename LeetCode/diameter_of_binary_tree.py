from typing import Optional


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    res = 0

    def dfs(node):
        nonlocal res
        if node is None:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)
        res = max(res, left + right)
        return max(1 + left, 1 + right)

    dfs(root)
    return res
