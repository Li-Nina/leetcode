class Solution:
    def sortColors(self, nums: 'List[int]') -> None:
        """
        Do not return anything, modify nums in-place instead.
        使用3个指针，分别代表当前位置，0的末尾，2的开头
        0 0 0 1 1 1 X X X 2 2 2
              |     |     |
            left   cur  right
        """

        def swap(array, i, j):
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

        cur = left = 0
        right = len(nums)
        while cur < right:
            if nums[cur] == 0:
                swap(nums, cur, left)
                left += 1
                cur += 1
            elif nums[cur] == 1:
                cur += 1
            else:
                swap(nums, cur, right - 1)
                right -= 1


if __name__ == '__main__':
    n = []
    Solution().sortColors(n)
    print(n)
