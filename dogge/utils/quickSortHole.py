#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    """
    2 4 5 1 3 9 8
    |           |
   left       right
   hole
   挖坑填数+分治，不需要swap
    """

    def sub_sort(self, nums: 'List[int]', left: int, right: int):
        if left < right:
            pivot = nums[left]
            hole = start = left
            end = right
            while left < right:
                if hole == left:
                    if nums[right] <= pivot:
                        nums[hole] = nums[right]
                        hole = right
                        left += 1
                    else:
                        right -= 1
                else:
                    if nums[left] >= pivot:
                        nums[hole] = nums[left]
                        hole = left
                        right -= 1
                    else:
                        left += 1
            nums[hole] = pivot
            self.sub_sort(nums, start, hole - 1)
            self.sub_sort(nums, hole + 1, end)

    def quick_sort(self, nums: 'List[int]'):
        self.sub_sort(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    l = [1, 2, 0, 9, 4, 8, 5, 2, 2, 8, -9, -5, -3, 2, 1, 1, 8, 9, 9, 0, 10]
    Solution().quick_sort(l)
    print(l)
