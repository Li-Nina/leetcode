class Solution:
    def setZeroes(self, matrix: 'List[List[int]]') -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        column = len(matrix)
        row = len(matrix[0])
        c_0 = False
        for c in range(column):
            if matrix[c][0] == 0:
                c_0 = True
                break
        r_0 = False
        for r in range(row):
            if matrix[0][r] == 0:
                r_0 = True
                break
        for c in range(1, column):
            for r in range(1, row):
                if matrix[c][r] == 0:
                    matrix[c][0] = 0
                    matrix[0][r] = 0
        for c in range(1, column):
            for r in range(1, row):
                if matrix[c][0] == 0 or matrix[0][r] == 0:
                    matrix[c][r] = 0
        if c_0:
            for c in range(column):
                matrix[c][0] = 0
        if r_0:
            for r in range(row):
                matrix[0][r] = 0
