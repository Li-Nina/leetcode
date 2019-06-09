# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insertIntoBST_recursion(self, root: TreeNode, val: int) -> TreeNode:
        def helper(node: TreeNode):
            if node.val > val:
                if not node.left:
                    node.left = TreeNode(val)
                else:
                    helper(node.left)
            else:
                if not node.right:
                    node.right = TreeNode(val)
                else:
                    helper(node.right)

        if not root:
            root = TreeNode(val)
        else:
            helper(root)
        return root

    def insertIntoBST_iteration(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            root = TreeNode(val)
        else:
            node = root
            while True:
                if node.val > val:
                    if node.left:
                        node = node.left
                    else:
                        node.left = TreeNode(val)
                        break
                else:
                    if node.right:
                        node = node.right
                    else:
                        node.right = TreeNode(val)
                        break
        return root
