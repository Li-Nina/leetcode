# Definition for a binary tree node.
"""
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rst = []

        def helper(node: TreeNode):
            if node:
                helper(node.left)
                rst.append(node.val)
                helper(node.right)

        helper(root)
        return rst

    def inorderTraversal_iteration(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rst = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                rst.append(root.val)
                root = root.right
        return rst
