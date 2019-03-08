# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> 'List[int]':
        rst = []
        stack = []
        while root or stack:
            if root:
                rst.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop().right
        return rst
