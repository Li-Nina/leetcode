class Solution:
    """
    [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]
    """

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix:
            c = 0
            c_len = len(matrix[0])
            r = len(matrix) - 1
            while r >= 0 and c < c_len:
                if matrix[r][c] == target:
                    return True
                elif matrix[r][c] > target:
                    r -= 1
                else:
                    c += 1
        return False

    def searchMatrix_recursion(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix and matrix[0]:
            if len(matrix) == 1 and len(matrix[0]) == 0:
                return matrix[0][0] == target
            r_len = len(matrix)
            c_len = len(matrix[0])
            c = c_len // 2
            r = 0
            while r < r_len and matrix[r][c] < target:
                r += 1
            if r < r_len and matrix[r][c] == target:
                return True
            else:
                if self.searchMatrix_recursion(list(map(lambda l: l[c + 1:], matrix[0:r])), target):
                    return True
                if self.searchMatrix_recursion(list(map(lambda l: l[0:c], matrix[r:])), target):
                    return True
        return False


if __name__ == '__main__':
    a = [[-1, 3]]
    y = Solution().searchMatrix_recursion(a, -1)
    print(y)
