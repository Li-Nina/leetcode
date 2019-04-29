# Definition for a binary tree node.
"""
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal_recursive(self, root: TreeNode) -> 'List[int]':
        rst = []

        def helper(node: TreeNode):
            if node:
                rst.append(node.val)
                helper(node.left)
                helper(node.right)

        helper(root)
        return rst

    def preorderTraversal_iteration(self, root: TreeNode) -> 'List[int]':
        rst = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                rst.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return rst
