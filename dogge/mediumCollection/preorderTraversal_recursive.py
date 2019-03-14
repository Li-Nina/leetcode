# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> 'List[int]':
        rst = []
        self.helper(root, rst)
        return rst

    def helper(self, node, rst):
        if node:
            rst.append(node.val)
            self.helper(node.left, rst)
            self.helper(node.right, rst)
