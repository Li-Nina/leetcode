class Solution:
    """
    2 4 5 1 3 9 8
    |           |
   left       right
   pivot
    """

    def quick_sort(self, nums: 'List[int]'):
        def sub_sort(_nums, start, end):
            if start < end:
                pivot = left = start
                right = end
                while left < right:
                    if pivot == left:
                        if _nums[right] >= _nums[pivot]:
                            right -= 1
                        else:
                            swap(_nums, right, pivot)
                            pivot = right
                    else:
                        if _nums[left] <= _nums[pivot]:
                            left += 1
                        else:
                            swap(_nums, left, pivot)
                            pivot = left
                sub_sort(_nums, start, left - 1)
                sub_sort(_nums, left + 1, end)

        def swap(_nums, i, j):
            temp = _nums[i]
            _nums[i] = _nums[j]
            _nums[j] = temp

        sub_sort(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    a = [2, 1, 9, 8, 5, 2, 4, 7, 4, 0]
    Solution().quick_sort(a)
    print(a)
