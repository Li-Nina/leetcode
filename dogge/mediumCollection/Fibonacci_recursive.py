import time


class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1 or N == 2:
            return 1
        else:
            return self.fib(N - 1) + self.fib(N - 2)


if __name__ == '__main__':
    s = time.time()
    x = Solution().fib(40)  # 计算40，耗时32秒，基本到极限
    print(x, time.time() - s)
