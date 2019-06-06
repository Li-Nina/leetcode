# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST_recursive(self, root: TreeNode, val: int) -> TreeNode:
        if not root or root.val == val:
            return root
        elif root.val > val:
            return self.searchBST_recursive(root.left, val)
        else:
            return self.searchBST_recursive(root.right, val)

    def searchBST_iteration(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
