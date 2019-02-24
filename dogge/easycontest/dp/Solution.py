class Solution:
    the_nums = None
    rob_sub_dict = {}

    def rob(self, nums: 'List[int]') -> 'int':
        self.the_nums = nums
        self.rob_sub_dict = {}
        return self.rob_sub(len(self.the_nums) - 1)

    def rob_sub(self, end_index: int) -> int:
        if end_index < 0:
            self.rob_sub_dict[end_index] = 0
            return 0
        # 判断rob_sub_dict某key存在，不能直接if rob_sub_dict.get(key)，因为值可能为0。if 0 == False
        n1 = self.rob_sub_dict[end_index - 1] if self.rob_sub_dict.get(end_index - 1) is not None else self.rob_sub(
            end_index - 1)
        n2 = self.rob_sub_dict[end_index - 2] + self.the_nums[end_index] if self.rob_sub_dict.get(
            end_index - 2) is not None else self.rob_sub(end_index - 2) + self.the_nums[end_index]
        self.rob_sub_dict[end_index] = max(n1, n2)
        return self.rob_sub_dict[end_index]


x = Solution().rob([0, 0, 0, 0])
print(x)
