# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# min_val = -4294967296
# max_val = 4294967296
# class Solution(object):
#     def isValidBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         return (self.isValidunit(root,min,max))
#     def isValidunit(self, root, min, max):
#         if root is None:
#             return True
#         if root.val <= min_val or root.val >= max_val:
#             return False
#         return (self.isValidunit(root.left, min_val, root.val) and self.isValidunit(root.right, root.val, max_val))


class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        mmin = -4294967296
        mmax = 4294967296
        return self.isValidBSTRange(root, mmin, mmax)

    def isValidBSTRange(self, root, mmin, mmax):
        if root == None:
            return True
        if root.val < mmax and root.val > mmin:
            LL = self.isValidBSTRange(root.left, mmin, root.val)
            RR = self.isValidBSTRange(root.right, root.val, mmax)
            return LL and RR
        else:
            return False
a = TreeNode(2)
b = TreeNode(1)
c = TreeNode(4)
d = TreeNode(1)
e = TreeNode(5)
a.left = b
a.right = c
c.left = d
c.right = e
print(Solution().isValidBST(a))