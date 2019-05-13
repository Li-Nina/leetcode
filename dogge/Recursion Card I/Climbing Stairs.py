class Solution:
    memo = []

    def climbStairs(self, n: int) -> int:
        if not self.memo:
            self.memo = [-1] * (n + 1)
        if self.memo[n] == -1:
            nums = 1 if n <= 1 else self.climbStairs(n - 1) + self.climbStairs(n - 2)
            self.memo[n] = nums
        return self.memo[n]


if __name__ == '__main__':
    x = Solution().climbStairs(50)
    print(x)
