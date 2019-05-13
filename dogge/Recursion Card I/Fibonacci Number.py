import functools


def memoization(func):
    known = dict()

    @functools.wraps(func)
    def memoizer(*args):
        if args not in known:
            known[args] = func(*args)
        return known[args]

    return memoizer


class Solution:
    @memoization
    def fib(self, N: int) -> int:
        if N <= 0:
            return 0
        elif N == 1:
            return 1
        else:
            return self.fib(N - 1) + self.fib(N - 2)


if __name__ == '__main__':
    x = Solution().fib(20)
    print(x)
