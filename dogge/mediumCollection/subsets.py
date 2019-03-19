class Solution:
    """
                 temp[  ]
             /      |     \
           [1]     [2]    [3]
         /    \     |
      [1,2] [1,3] [2,3]
       /
    [1,2,3]
    """

    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        rst = []

        def backtracking(temp, index):
            rst.append(temp[:])
            for i in range(index, len(nums)):
                temp.append(nums[i])
                backtracking(temp, i + 1)
                temp.pop()

        backtracking([], 0)
        return rst


if __name__ == '__main__':
    r = Solution().subsets([1, 2, 3])
    print(r)
