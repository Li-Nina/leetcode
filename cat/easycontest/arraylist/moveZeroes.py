class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n=0
        while 0 in nums:
            nums.remove(0)
            n+=1
        for i in range(n):
            nums.append(0)


