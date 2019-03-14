# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rst = []
        self.helper(root, rst)
        return rst

    def helper(self, node, rst):
        if node:
            self.helper(node.left, rst)
            self.helper(node.right, rst)
            rst.append(node.val)
