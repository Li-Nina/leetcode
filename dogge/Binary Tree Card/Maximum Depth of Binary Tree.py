# Definition for a binary tree node.
"""
    3
   / \
  9  20
    /  \
   15   7
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.depth = 0

    def maxDepth_topDown(self, root: TreeNode) -> int:
        def topDown(node: TreeNode, num):
            if node:
                topDown(node.left, num + 1)
                topDown(node.right, num + 1)
            else:
                self.depth = max(self.depth, num)

        topDown(root, 0)
        return self.depth

    # bottom-up
    def maxDepth(self, root: TreeNode) -> int:
        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1) if root else 0
