# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal_recursion(self, root: TreeNode) -> 'List[int]':
        rst = []

        def inorder(node: TreeNode):
            if node:
                inorder(node.left)
                rst.append(node.val)
                inorder(node.right)

        inorder(root)
        return rst

    def inorderTraversal_iteration(self, root: TreeNode) -> 'List[int]':
        rst = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            rst.append(root.val)
            root = root.right
        return rst
