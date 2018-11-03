# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# min_val = -4294967296
# max_val = 4294967296
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        res = []
        tree_inorder = self.inorder(root, res)
        if tree_inorder:
            pre = tree_inorder[0]
            for i in tree_inorder[1:]:
                if pre < i:
                    pre = i
                else:
                    return False
        return True

    def inorder(self, tree, res):
        if tree:
            self.inorder(tree.left, res)
            res.append(tree.val)
            self.inorder(tree.right, res)
            return res


# class Solution:
#     # @param root, a tree node
#     # @return a boolean
#     def isValidBST(self, root):
#         mmin = -float('inf')
#         mmax = float('inf')
#         return self.isValidBSTRange(root, mmin, mmax)
#
#     def isValidBSTRange(self, root, mmin, mmax):
#         if root == None:
#             return True
#         #为了判断当前节点和父节点的关系
#         elif not mmin < root.val < mmax:
#             return False
#         #为了判断当前节点和子节点的关系
#         return (self.isValidBSTRange(root.left, mmin, root.val)) and (self.isValidBSTRange(root.right, root.val, mmax))
# a = TreeNode(2)
# b = TreeNode(1)
# c = TreeNode(4)
# d = TreeNode(1)
# e = TreeNode(5)
# a.left = b
# a.right = c
# c.left = d
# c.right = e
# print(Solution().isValidBST(a))


a=[1,2,3]
x = a[10:]
print(x)