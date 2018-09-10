from collections import Counter


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        b = []
        nums1.sort()
        nums2.sort()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                b.append(nums2[i])
                i += 1
                j += 1
        return b

    def intersect2(self, nums1, nums2):
        a, b = map(Counter, (nums1, nums2))
        # c=a&b
        return list((a & b).elements())


a1 = [4, 4, 9, 5]
b1 = [9, 4, 9, 8, 4]
print(Solution().intersect2(a1, b1))
