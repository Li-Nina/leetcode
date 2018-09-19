class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # n = 0
        # while 0 in nums:
        #     nums.remove(0)
        #     n += 1
        # for i in range(n):
        #     nums.append(0)
        point = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[point], nums[i] = nums[i], nums[point]
                point += 1



if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    a[0], a[1], a[2] = a[1], a[2], a[3]
    print(a)
