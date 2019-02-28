class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        result = []
        if nums:
            nums.sort()
            i = 0  # base_index
            while i < len(nums) - 2:
                base_index = i
                right_index = len(nums) - 1
                left_index = i + 1
                while left_index < right_index:
                    _sum = nums[base_index] + nums[left_index] + nums[right_index]
                    if _sum < 0:
                        left_index = self.left_forward(left_index, nums, right_index)
                    elif _sum > 0:
                        right_index = self.right_backward(left_index, nums, right_index)
                    else:
                        result.append([nums[base_index], nums[left_index], nums[right_index]])
                        left_index = self.left_forward(left_index, nums, right_index)
                        right_index = self.right_backward(left_index, nums, right_index)
                i = self.base_forward(base_index, i, nums)
        return result

    def base_forward(self, base_index, i, nums):
        i += 1
        while i < len(nums) - 2 and nums[base_index] == nums[i]:
            i += 1
        return i

    def right_backward(self, left_index, nums, right_index):
        while right_index > left_index and nums[right_index] == nums[right_index - 1]:
            right_index -= 1
        right_index -= 1
        return right_index

    def left_forward(self, left_index, nums, right_index):
        while left_index < right_index and nums[left_index] == nums[left_index + 1]:
            left_index += 1
        left_index += 1
        return left_index


if __name__ == '__main__':
    pass
