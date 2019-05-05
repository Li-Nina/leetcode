# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Our base cases.
        How our recursion stops.
        When we have an answer.

        1.) If the node we are holding is null then we can't search...just return null
        2.) If we find either value return ourselves to the caller
        Remember, we are "grabbing"/"holding" 'root' in this call.
        """
        if not root or root == p or root == q:
            return root
        """
        'root' doesn't satisfy any of our base cases.
        Search left and then search right.
        """
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is None:
            """
            If nothing turned up on the left, return whatever we got
            back on the right
            """
            return right
        elif right is None:
            """
            If nothing turned up on the right, return whatever we got
            back on the left.
            """
            return left
        else:
            """
            If we reach here that means we got something back on the left AND
            right...that means this node is the LCA...because our recursion returns
            from bottom to up...so we return what we hold...'root'
            """
            return root
