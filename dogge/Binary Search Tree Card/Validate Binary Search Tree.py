# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node: TreeNode, lnum, rnum):
            if node is None:
                return True
            if lnum < node.val < rnum:
                return helper(node.left, lnum, node.val) and helper(node.right, node.val, rnum)
            else:
                return False

        return helper(root, float('-inf'), float('inf'))

    def isValidBST_iteration(self, root: TreeNode) -> bool:
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, lnum, rnum = stack.pop()
            if node:
                if node.val <= lnum or node.val >= rnum:
                    return False
                stack.append((node.left, lnum, node.val))
                stack.append((node.right, node.val, rnum))
        return True
