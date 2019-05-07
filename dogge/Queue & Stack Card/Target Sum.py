class Solution:
    # todo wrong ans
    def findTargetSumWays_recusive(self, nums: 'List[int]', S: int) -> int:
        length = len(nums)

        def helper(cur, num):
            if cur == length:
                return 1 if num == S else 0
            else:
                return helper(cur + 1, num + nums[cur]) + helper(cur + 1, num - nums[cur])

        return helper(0, 0)

    def findTargetSumWays(self, nums: 'List[int]', S: int) -> int:
        length = len(nums)

        def helper(cur, num):
            if cur == length:
                return 1 if num == S else 0
            else:
                return helper(cur + 1, num + nums[cur]) + helper(cur + 1, num - nums[cur])

        return helper(0, 0)


if __name__ == '__main__':
    x = Solution().findTargetSumWays([1, 1, 1, 1, 1], 3)
    print(x)
