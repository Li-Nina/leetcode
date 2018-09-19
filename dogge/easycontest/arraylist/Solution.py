class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        result = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1
        return result

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {val: i for (i, val) in enumerate(nums)}
        for i, val in enumerate(nums):
            j = dic.get(target - val)
            if j is not None and j != i:
                return [i, j]

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()
        for index, val in enumerate(nums):
            j = dic.get(target - val)
            if j is not None and j != index:
                return [j, index]
            dic[val] = index

    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


nums = [1, 2, 3, 4, 5]
print nums[:-2]

# a = {10: 2}
# print (a.get(10))
