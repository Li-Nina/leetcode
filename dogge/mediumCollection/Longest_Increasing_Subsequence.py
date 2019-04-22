class Solution:
    def lengthOfLIS(self, nums: 'List[int]') -> int:
        """
        Input: [10,9,2,5,3,7,101,18]
        Output: 4
        Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
        """
        memo = {}

        def subLIS(index: int):
            """
            最后一位为index的lengthOfLIS
            """
            if index in memo:
                return memo[index]
            longest = 1
            for i in range(index):
                if nums[index] > nums[i] and subLIS(i) + 1 > longest:
                    longest = subLIS(i) + 1
            memo[index] = longest
            return longest

        if nums:
            lis_list = [subLIS(i) for i in range(len(nums))]
            return max(lis_list)
        else:
            return 0


if __name__ == '__main__':
    r = Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
    print(r)
