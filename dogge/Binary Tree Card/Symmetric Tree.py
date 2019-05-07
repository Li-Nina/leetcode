# Definition for a binary tree node.
"""
    1            1
   / \          / \
  2   2        2   2
 / \ / \        \   \
3  4 4  3       3    3
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric_recursive(self, root: TreeNode) -> bool:
        def recursive(left: TreeNode, right: TreeNode):
            if left is None or right is None:
                return left == right
            elif left.val != right.val:
                return False
            else:
                return recursive(left.left, right.right) and recursive(left.right, right.left)

        if root is None:
            return True
        return recursive(root.left, root.right)

    def isSymmetric_iteration(self, root: TreeNode) -> bool:
        if root is None:
            return True
        lstack = [root.left]
        rstack = [root.right]
        while lstack:
            left = lstack.pop()
            right = rstack.pop()
            if left is None or right is None:
                if left != right:
                    return False
            elif left.val != right.val:
                return False
            else:
                lstack.append(left.left)
                lstack.append(left.right)
                rstack.append(right.right)
                rstack.append(right.left)
        return True
