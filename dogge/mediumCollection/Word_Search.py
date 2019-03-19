class Solution:
    def exist(self, board: 'List[List[str]]', word: str) -> bool:
        row_num = len(board)
        column_num = len(board[0])

        def backtracking(row, column, index, seen):
            if row > row_num - 1 or row < 0 or column > column_num - 1 \
                    or column < 0 or (row, column) in seen or board[row][column] != word[index]:
                return False
            elif index == len(word) - 1:
                return True
            else:
                seen.add((row, column))
                if backtracking(row + 1, column, index + 1, seen) or \
                        backtracking(row - 1, column, index + 1, seen) or \
                        backtracking(row, column + 1, index + 1, seen) or \
                        backtracking(row, column - 1, index + 1, seen):
                    return True
                else:
                    seen.remove((row, column))
                    return False

        for i in range(row_num):
            for j in range(column_num):
                seen = set()
                if backtracking(i, j, 0, seen):
                    return True
        return False


if __name__ == '__main__':
    x = Solution().exist([["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCESEEEFS")
    print(x)
