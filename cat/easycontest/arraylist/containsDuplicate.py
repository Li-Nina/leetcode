class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        my_set = set()
        for num in nums:
            if num in my_set:
                return True
            else:
                my_set.add(num)
        return False
