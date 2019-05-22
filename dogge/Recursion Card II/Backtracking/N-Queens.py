class Solution:
    """
        [".Q..",
         "...Q",
         "Q...",
         "..Q."]
    """

    def __init__(self):
        self.placed = []
        self.rst = []

    def solveNQueens(self, n: int) -> 'List[List[str]]':
        self.backtracking(0, n)
        return self.rst

    def backtracking(self, row: int, n: int):
        if row == n:
            self.addSolution(n)
        else:
            for c in range(n):
                if self.isValid(row, c):
                    self.placeQueen(c)
                    self.backtracking(row + 1, n)
                    self.undoPlaceQueen()

    def addSolution(self, n: int):
        solution = []
        for c in self.placed:
            solution.append('.' * c + 'Q' + '.' * (n - c - 1))
        self.rst.append(solution)

    def isValid(self, row, c):
        for r_, c_ in enumerate(self.placed):
            if c == c_ or c == c_ + (row - r_) or c == c_ - (row - r_):
                return False
        return True

    def placeQueen(self, column):
        self.placed.append(column)

    def undoPlaceQueen(self):
        self.placed.pop()


if __name__ == '__main__':
    x = Solution().solveNQueens(8)
    print(x)
