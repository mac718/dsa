from typing import Optional


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    def dfs(node):
        if node is None:
            return 0
        return max(1 + dfs(node.left), 1 + dfs(node.right))
    left = dfs(root.left)
    right = dfs(root.right)

    return right + left

