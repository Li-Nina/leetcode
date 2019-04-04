class Solution:

    def searchMatrix_matrix(self, matrix: 'List[List[int]]', target: int) -> bool:
        """
        two times binary search,log(m)+log(n)
        """

        def binary_search(target, array, equal):
            floor = -1
            left = 0
            right = len(array) - 1
            while left <= right:
                mid = (left + right) // 2
                if target > array[mid]:
                    left = mid + 1
                    floor = mid
                elif target < array[mid]:
                    right = mid - 1
                else:
                    return mid
            return -1 if equal else floor

        if matrix and matrix[0]:
            column_0 = [row[0] for row in matrix]
            row_num = binary_search(target, column_0, False)
            return binary_search(target, matrix[row_num], True) > -1
        return False

    def searchMatrix_sortedArray(self, matrix: 'List[List[int]]', target: int) -> bool:
        """
        one time binary search，log(mn)
        """
        if matrix and matrix[0]:
            row_num = len(matrix)
            column_num = len(matrix[0])
            left = 0
            right = row_num * column_num - 1
            while left <= right:
                mid = (left + right) // 2
                row = mid // column_num
                column = mid % column_num
                if target > matrix[row][column]:
                    left = mid + 1
                elif target < matrix[row][column]:
                    right = mid - 1
                else:
                    return True
        return False
