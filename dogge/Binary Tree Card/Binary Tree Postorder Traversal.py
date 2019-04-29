# Definition for a binary tree node.
"""
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal_recursive(self, root: TreeNode) -> 'List[int]':
        rst = []

        def helper(node: TreeNode):
            if node:
                helper(node.left)
                helper(node.right)
                rst.append(node.val)

        helper(root)
        return rst

    def postorderTraversal_iteration(self, root: TreeNode) -> 'List[int]':
        rst = []
        stack = []
        while root or stack:
            if root:
                rst.insert(0, root.val)
                stack.append(root)
                root = root.right
            else:
                root = stack.pop().left
        return rst
