# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def find(node: TreeNode, root_val: int):
            if not node:
                return -1
            if node.val != root_val:
                return node.val
            left = find(node.left, root_val)
            right = find(node.right, root_val)
            return min(left, right) if not (left == -1 or right == -1) else max(left, right)

        l = find(root.left, root.val)
        r = find(root.right, root.val)
        return min(l, r) if not (l == -1 or r == -1) else max(l, r)
