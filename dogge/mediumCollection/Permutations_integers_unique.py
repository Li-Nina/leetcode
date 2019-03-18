import collections

"""
    有问题，暂缓
"""


class Solution:
    def permuteUnique(self, nums: 'List[int]') -> 'List[List[int]]':
        rst = []
        rst_dict = collections.defaultdict(set)

        def backtracking(temp_list):
            if len(temp_list) == len(nums):
                temp = temp_list[:]
                rst.append(temp)
                return
            for num in nums:
                if num not in rst_dict[len(temp_list)]:
                    rst_dict[len(temp_list)].add(num)
                    print(rst_dict)
                    temp_list.append(num)
                    backtracking(temp_list)
                    temp_list.pop()

        backtracking([])
        print(rst_dict)
        return rst


if __name__ == '__main__':
    x = Solution().permuteUnique([1, 2, 3])
    print(x)
