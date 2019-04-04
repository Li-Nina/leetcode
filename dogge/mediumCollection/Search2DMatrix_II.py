class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix and matrix[0]:
            row_num = len(matrix)
            column_num = len(matrix[0])
            r = row_num - 1
            c = 0
            while row_num > r >= 0 and column_num > c:
                if matrix[r][c] > target:
                    r -= 1
                elif matrix[r][c] < target:
                    c += 1
                else:
                    return True
        return False
