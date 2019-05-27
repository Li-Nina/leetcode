class Solution:
    """
    Diagonal row+col is same
    """

    def findDiagonalOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        rst = []
        if matrix and matrix[0]:
            M = len(matrix)
            N = len(matrix[0])
            times = 0
            for sums in range((M - 1) + (N - 1) + 1):
                if times % 2 == 0:
                    for i in range(sums, -1, -1):
                        if i < M and sums - i < N:
                            rst.append(matrix[i][sums - i])
                else:
                    for i in range(sums + 1):
                        if i < M and sums - i < N:
                            rst.append(matrix[i][sums - i])
                times += 1
        return rst


if __name__ == '__main__':
    x = Solution().findDiagonalOrder(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    )
    print(x)
