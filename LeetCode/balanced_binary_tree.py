from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root: Optional[TreeNode]) -> bool:
    def dfs(self, node):
        if node is None:
            return 0
        return max(1 + self.dfs(node.left), 1 + self.dfs(node.right))


def compare(self, node):
    left = self.dfs(node.left)
    right = self.dfs(node.right)
    if left > right + 1 or left < right - 1:
        return False
    return True


def traverse(self, node):
    if not self.compare(node):
        return False
    if node.left:
        if not self.traverse(node.left):
            return False
    if node.right:
        if not self.traverse(node.right):
            return False
    return True


def isBalanced(self, root: Optional[TreeNode]) -> bool:
    if not root:
        return True
    return self.traverse(root)