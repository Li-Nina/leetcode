class Solution:
    def pivotIndex(self, nums: 'List[int]') -> int:
        s = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            left_sum += 0 if i == 0 else nums[i - 1]
            right_sum = s - left_sum - nums[i]
            if left_sum == right_sum:
                return i
        return -1


if __name__ == '__main__':
    x = Solution().pivotIndex([1])
    print(x)
