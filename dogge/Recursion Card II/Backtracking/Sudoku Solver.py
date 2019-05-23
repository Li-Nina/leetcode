class Solution:
    def solveSudoku(self, board: 'List[List[str]]') -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def backtracking(row: int, column: int):
            if row == 9:
                return True
            elif board[row][column] == ".":
                for i in range(1, 10):
                    if isValid(str(i), row, column):
                        board[row][column] = str(i)
                        r, c = (row + 1, 0) if column + 1 == 9 else (row, column + 1)
                        if backtracking(r, c):
                            return True
                        else:
                            board[row][column] = "."
                return False
            else:
                r, c = (row + 1, 0) if column + 1 == 9 else (row, column + 1)
                return backtracking(r, c)

        def isValid(i, row, column):
            if i in board[row]:
                return False
            if i in [r[column] for r in board]:
                return False
            r_ = (row // 3) * 3
            c_ = (column // 3) * 3
            b_ = [board[i][c_:c_ + 3] for i in range(r_, r_ + 3)]
            for b_row in b_:
                if i in b_row:
                    return False
            return True

        backtracking(0, 0)


if __name__ == '__main__':
    t = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    Solution().solveSudoku(t)
    print(t)
