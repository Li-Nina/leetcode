class Solution:
    mapping = ((0, 1), (1, 0))

    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        return self.mapping[self.kthGrammar(N - 1, K // 2 + K % 2)][(K - 1) % 2]


if __name__ == '__main__':
    x = Solution().kthGrammar(2, 1)
    print(x)

    print(5 // 2 + 5 % 2)
    print(5 % 2)
