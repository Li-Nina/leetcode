class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        i=0
        j = 0
        b = []
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    b.append(i)
                    b.append(j)
                    return b
                j += 1
            i += 1
        '''
        '''
        dic = {val:i for (i, val) in enumerate(nums)}
        for i, v in dic.items():
            j = dic.get(target-i)
            if (j is not None and j!=v ):
                return [v,j]
        '''
        dic = dict()
        for i, num in enumerate(nums):
            j = dic.get(target - num)
            if j is not None and j != i:
                return [j, i]
            dic[num] = i


a = [3, 2, 4]
print(Solution().twoSum(a, 6))
