class Solution:
    def isToeplitzMatrix(self, matrix: 'List[List[int]]') -> bool:
        length = len(matrix[0])

        def cmp(r1, r2):
            for i in range(length - 1):
                if r1[i] != r2[i]:
                    return False
            return True

        previous = matrix[0]
        for row in matrix[1:]:
            if not cmp(previous[0:length - 1], row[1:]):
                return False
            else:
                previous = row
        return True
