class Solution:
    def generate(self, numRows: int) -> 'List[List[int]]':
        if numRows <= 0:
            return []
        rst = [[0 for _ in range(i + 1)] for i in range(numRows)]
        rst[0][0] = 1

        def recursive(row: int, column: int):
            if rst[row][column]:
                return rst[row][column]
            else:
                if column == 0 or column == row:
                    rst[row][column] = 1
                    return 1
                else:
                    num = recursive(row - 1, column - 1) + recursive(row - 1, column)
                    rst[row][column] = num
                    return num

        for i in range(numRows):
            recursive(numRows - 1, i)
        return rst

    def generate_iteration(self, numRows: int) -> 'List[List[int]]':
        if numRows <= 0:
            return []
        rst = [[0 for _ in range(i + 1)] for i in range(numRows)]
        rst[0][0] = 1

        for i in range(numRows):
            for j in range(i + 1):
                rst[i][j] = 1 if j == 0 or j == i else rst[i - 1][j - 1] + rst[i - 1][j]
        return rst


if __name__ == '__main__':
    x = Solution().generate_iteration(1)
    print(x)
