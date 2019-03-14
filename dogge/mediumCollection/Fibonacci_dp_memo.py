import sys
import time


class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        memo = [0] * (N + 1)
        return self.helper(N, memo)

    def helper(self, N, memo):
        if memo[N]:
            return memo[N]
        if N == 1 or N == 2:
            result = 1
        else:
            result = self.helper(N - 1, memo) + self.helper(N - 2, memo)
        memo[N] = result
        return result


if __name__ == '__main__':
    maximum_recursion_depth = sys.getrecursionlimit()
    print('maximum_recursion_depth is {}'.format(maximum_recursion_depth))
    s = time.time()
    x = Solution().fib(998)  # 秒出，但是有最大递归深度限制，1000
    print(x, time.time() - s)
