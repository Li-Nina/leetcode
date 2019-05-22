# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.valid(root, float('inf'), float('-inf'))

    def valid(self, node: TreeNode, big, small):
        if node.left:
            b = big
            if node.val < big:
                b = node.val
            l_bst = b > node.left.val > small and self.valid(node.left, b, small)
        else:
            l_bst = True

        if node.right:
            s = small
            if node.val > small:
                s = node.val
            r_bst = big > node.right.val > s and self.valid(node.right, big, s)
        else:
            r_bst = True

        return l_bst and r_bst

    def isValidBST_concise(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)
