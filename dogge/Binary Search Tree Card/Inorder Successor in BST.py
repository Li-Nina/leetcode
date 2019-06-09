"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """

    def inorderSuccessor(self, root, p):
        def right_least(right):
            while right.left:
                right = right.left
            return right

        def nearest_left_parent(node, p):
            parent = None
            while True:
                if node == p:
                    return parent
                elif node.val > p.val:
                    parent = node
                    node = node.left
                else:
                    node = node.right

        if not p:
            return None
        if p.right:
            successor = right_least(p.right)
        else:
            successor = nearest_left_parent(root, p)

        return successor
