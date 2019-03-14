# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        rst = []
        stack = [root]
        length = 0
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                rst.append(node.val)
                root = node.right
                length += 1
                if length == k:
                    return node.val
