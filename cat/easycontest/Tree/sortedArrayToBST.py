# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)==0:
            return None
        elif len(nums)==1:
            return TreeNode(nums[0])#注意不是nums,因为是取其值，而不是[-3,10,[4]0,5]
        else:
            mid = len(nums)/2#只要满足二叉树就行，没有标准的唯一答案
            root=TreeNode(nums[mid])
            num1 = nums[0:mid]
            num2 = nums[mid+1:]
            root.left = self.sortedArrayToBST(num1)
            root.right = self.sortedArrayToBST(num2)
            return root

