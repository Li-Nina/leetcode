class Solution:
    def dominantIndex(self, nums: 'List[int]') -> int:
        rst = -1
        largest = 0
        for i in range(len(nums)):
            if nums[i] > largest:
                rst = i if nums[i] >= 2 * largest else -1
                largest = nums[i]
            elif nums[i] * 2 > largest:
                rst = -1
        return rst


if __name__ == '__main__':
    x = Solution().dominantIndex([0, 0, 3, 2])
    print(x)
