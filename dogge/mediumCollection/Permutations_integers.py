class Solution:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        rst = []

        def backtracking(temp_list):
            if len(temp_list) == len(nums):
                rst.append(temp_list[:])
                return
            for i in nums:
                if i not in temp_list:
                    temp_list.append(i)
                    backtracking(temp_list)
                    temp_list.pop()

        backtracking([])
        return rst


if __name__ == '__main__':
    x = Solution().permute([1, 2, 3, 4])
    print(x)
