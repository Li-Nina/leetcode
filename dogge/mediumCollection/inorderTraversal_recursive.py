# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rst = []
        self.helper(rst, root)
        return rst

    def helper(self, rst, node):
        if node:
            self.helper(rst, node.left)
            rst.append(node.val)
            self.helper(rst, node.right)
