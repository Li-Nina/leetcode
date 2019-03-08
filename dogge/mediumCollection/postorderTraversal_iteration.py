# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
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
