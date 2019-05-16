class Solution:
    def sortArray(self, nums: 'List[int]') -> 'List[int]':
        self.qsort(nums, 0, len(nums) - 1)
        return nums

    def qsort(self, nums: 'List[int]', left: int, right: int):
        if left < right:
            pivot = self.partition(nums, left, right)
            self.qsort(nums, left, pivot - 1)
            self.qsort(nums, pivot + 1, right)

    def partition(self, nums: 'List[int]', left: int, right: int):
        pivot = right
        i = left  # 大于pivot的最左index
        for j in range(left, right):
            if nums[j] < nums[pivot]:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        nums[i], nums[pivot] = nums[pivot], nums[i]
        return i


if __name__ == '__main__':
    x = Solution().sortArray([200, 3, 8, 9, 1, 1, 5, 7])
    print(x)
