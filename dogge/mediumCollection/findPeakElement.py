class Solution:
    def findPeakElement_(self, nums: 'List[int]') -> int:
        nums.append(float("-inf"))
        nums.insert(0, float("-inf"))
        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] > nums[i + 1]:
                return i - 1

    def findPeakElement(self, nums: 'List[int]') -> int:
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1

    def findPeakElement_binarySearch(self, nums: 'List[int]') -> int:
        def helper(nums, start, end):
            if start == end:
                return start
            else:
                mid = (start + end) // 2
                return helper(nums, start, mid) if nums[mid] > nums[mid + 1] else helper(nums, mid + 1, end)

        return helper(nums, 0, len(nums) - 1)

    def findPeakElement_binarySearch_iteration(self, nums: 'List[int]') -> int:
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid + 1
        return start


if __name__ == '__main__':
    m = Solution().findPeakElement_binarySearch_iteration([1, 2, 3, 1])
    print(m)
