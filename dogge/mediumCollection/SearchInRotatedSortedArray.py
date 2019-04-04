class Solution:
    def search(self, nums: 'List[int]', target: int) -> int:
        if nums:
            first = nums[0]
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if target > nums[mid]:
                    if nums[mid] < first <= target:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif target < nums[mid]:
                    if nums[mid] >= first > target:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    return mid
        return -1


if __name__ == '__main__':
    x = Solution().search([1, 3], 3)
    print(x)
