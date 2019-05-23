class Solution:
    """
    Input: n = 4, k = 2
    Output:
    [
      [2,4],
      [3,4],
      [2,3],
      [1,2],
      [1,3],
      [1,4],
    ]
    """

    def combine(self, n: int, k: int) -> 'List[List[int]]':
        rst = []

        def backtracking(slist: 'List[int]', cur: int):
            if len(slist) == k:
                rst.append(slist[:])
            else:
                for num in range(cur + 1, n + 1):
                    slist.append(num)
                    backtracking(slist, num)
                    slist.pop()

        backtracking([], 0)
        return rst


if __name__ == '__main__':
    t = Solution().combine(4, 2)
    print(t)
