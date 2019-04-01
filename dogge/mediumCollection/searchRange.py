import math


class Solution:
    def searchRange(self, nums: 'List[int]', target: int) -> 'List[int]':
        index = 0
        length = len(nums)
        left = right = -1
        while index < length and right == -1:
            if nums[index] == target and left == -1:
                left = index
            elif nums[index] != target and left != -1:
                right = index - 1
            index += 1
        if left != -1 and right == -1:
            right = length - 1
        return [left, right]

    def searchRange_binarySearch(self, nums: 'List[int]', target: int) -> 'List[int]':
        # find lmost
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        if right != -1 and nums[left] == target:
            lmost = left
            right = len(nums) - 1
        else:
            return [-1, -1]
        # find rmost
        while left < right:
            mid = math.ceil((left + right) / 2)
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] <= target:
                left = mid
        return [lmost, right]


if __name__ == '__main__':
    x = Solution().searchRange_binarySearch([1, 1, 1, 1, 2, 2, 2, 3, 7, 8, 9, 9], 0)
    print(x)
