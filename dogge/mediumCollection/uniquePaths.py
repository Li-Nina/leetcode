class Solution:
    def uniquePaths2(self, m: int, n: int) -> int:
        def backtracking(j: int, k: int, rst: int):
            if j == m - 1 and k == n - 1:
                rst += 1
                return rst
            if j > m - 1 or k > n - 1:
                return rst
            return backtracking(j + 1, k, rst) + backtracking(j, k + 1, rst)

        return backtracking(0, 0, 0)

    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def path(j: int, k: int):
            if j == 1 and k == 1:
                return 1
            if j < 1 or k < 1:
                return 0
            left = memo[(j - 1, k)] if memo.get((j - 1, k)) else path(j - 1, k)
            up = memo[(j, k - 1)] if memo.get((j, k - 1)) else path(j, k - 1)
            val = left + up
            memo[(j, k)] = val
            return val

        return path(m, n)


if __name__ == '__main__':
    x = Solution().uniquePaths(300, 300)
    print(x)
