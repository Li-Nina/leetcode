#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Solution:
    def intersection(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        return list(set(nums1) & set(nums2))

    def intersection2(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        return [n for n in nums2 if n in set(nums1)]


if __name__ == '__main__':
    print(Solution().intersection([1, 2, 3, 4, 5], [3, 4, 8, 9, 0]))
    print(Solution().intersection2([1, 2, 3, 4, 5], [3, 4, 8, 9, 0]))
