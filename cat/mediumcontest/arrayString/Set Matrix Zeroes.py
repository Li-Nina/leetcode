# class Solution(object):
#     def setZeroes(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: None Do not return anything, modify matrix in-place instead.
#         """
#         m = len(matrix)
#         n = len(matrix[0])
#         row = [False for i in range(m)]
#         col = [False for j in range(n)]
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == 0:
#                     row[i] = True
#                     col[j] = True
#         for i in range(m):
#             for j in range(n):
#                 if row[i] or col[j]:
#                     matrix[i][j] = 0
#由于把所有matrix[i][j]==0，则立flag，matrix[i][o]=0,matrix[o][j]=0.由于matrix[0][0]只能表示行或者列，所以列要单独用变量is_col来表示
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        is_col = False
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j] == 0:
                    matrix[i][j]=0
        if matrix[0][0]==0:
            for j in range(n):
                matrix[0][j]=0
        if is_col:
            for i in range(m):
                matrix[0][j]=0

ma = [[1,2,3,5,0],[2,4,6,7,9],[4,3,0,7,6]]
aa = Solution()
aa.setZeroes(ma)
print(ma)
