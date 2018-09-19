class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b = sorted(nums)
        for i, v in enumerate(b[:-1]):
            if i % 2 == 0:
                if b[i] != b[i + 1]:
                    return b[i]
        return b[-1]

    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_set = set()
        for i in nums:
            if i in my_set:
                my_set.remove(i)
            else:
                my_set.add(i)
        return my_set.pop()

    def singleNumber3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a



A = [4, 1, 2, 1, 2]
print(sorted(A))
print(Solution().singleNumber(A))
