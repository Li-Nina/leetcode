class Solution:
    def reverse(self, nums, start, end):
        while start < end:
            temp = nums[end]
            nums[end] = nums[start]
            nums[start] = temp
            start += 1
            end -= 1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)


A = [1, 2, 3, 4, 5, 6, 7]
a = Solution().rotate(A, 3)
print(a)
