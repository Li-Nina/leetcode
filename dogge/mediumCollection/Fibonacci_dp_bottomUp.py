import time


class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1 or N == 2:
            return 1
        memo = [0] * (N + 1)
        memo[1] = 1
        memo[2] = 1
        for i in range(3, N + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[N]

    def fib_iter(self, N: int) -> int:
        if N == 0:
            return 0
        a = 1
        b = 1
        for i in range(3, N + 1):
            c = a + b
            a = b
            b = c
        return b


if __name__ == '__main__':
    s = time.time()
    x = Solution().fib(100000)  # 秒出
    print(x, time.time() - s)
