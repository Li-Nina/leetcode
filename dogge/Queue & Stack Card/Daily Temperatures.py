import sys


class Solution:
    def dailyTemperatures_inverse(self, T: 'List[int]') -> 'List[int]':
        """
        The length of temperatures will be in the range [1, 30000].
        Each temperature will be an integer in the range [30, 100].
        rst={val:minIndex}
        """
        nst = [sys.maxsize for _ in range(102)]
        rst = [0 for _ in range(len(T))]
        for i in range(len(T) - 1, -1, -1):
            warmer_index = min(j for j in nst[T[i] + 1: 102])
            if warmer_index < sys.maxsize:
                rst[i] = warmer_index - i
            nst[T[i]] = i
        return rst

    def dailyTemperatures_stack(self, T: 'List[int]') -> 'List[int]':
        """
        The length of temperatures will be in the range [1, 30000].
        Each temperature will be an integer in the range [30, 100].
        """
        rst = [0 for _ in range(len(T))]
        stack = []

        for i, v in enumerate(T):
            while stack and stack[-1][0] < v:
                v_, i_ = stack.pop()
                rst[i_] = i - i_
            stack.append((v, i))
        return rst


if __name__ == '__main__':
    x = Solution().dailyTemperatures_inverse([89, 62, 70, 58, 47, 47, 46, 76, 100, 70])
    print(x)
    x = Solution().dailyTemperatures_stack([89, 62, 70, 58, 47, 47, 46, 76, 100, 70])
    print(x)
