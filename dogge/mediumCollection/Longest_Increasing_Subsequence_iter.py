class Solution:
    def lengthOfLIS(self, nums: 'List[int]') -> int:
        """
        Input: [10,9,2,5,3,7,101,18]
        Output: 4
        Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
        """
        if not nums:
            return 0
        lis_list = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and lis_list[j] + 1 > lis_list[i]:
                    lis_list[i] = lis_list[j] + 1
        return max(lis_list)


if __name__ == '__main__':
    r = Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
    print(r)
