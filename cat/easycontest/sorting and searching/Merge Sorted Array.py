class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        index = m+n-1
        index1 = m-1
        index2 = n-1
        while (index1>=0 and index2>=0):
            if nums1[index1]<=nums2[index2]:
                nums1[index] = nums2[index2]
                index-=1
                index2-=1
            else:
                nums1[index] = nums1[index1]
                index1-=1
                index-=1
        while index2>=0:
            nums1[index] = nums2[index2]
            index-=1
            index2-=1
a = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
a.merge(nums1,3,nums2,3)
print(nums1)
