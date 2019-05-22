class Solution:
    """
    The 3 Keys To Backtracking Problems:

    Our Choice

    -) What choice are we making at each call of the function
    -) RECURSION REPRESENTS A DECISION.
    -) RECURSION REPRESENTS A CHOICE & its associated state
    -) Each function call represents a state. From that state decisions can be made.

    Our Constraints

    -) What tells us to stop following a certain path that we are searching on?
    -) Have we exhausted all possibilities?

    Our Goal

    -) What is our target?
    -) What are we trying to find?
    -) These will craft our base cases.
    """

    def __init__(self):
        self.placed = set()

    def totalNQueens(self, n: int) -> int:
        return self.backtracking(0, n, 0)

    def backtracking(self, row: int, n: int, count: int):
        if row == n:
            count += 1
        else:
            for c in range(n):
                if self.isValid(row, c):
                    self.placeQueen(row, c)
                    count = self.backtracking(row + 1, n, count)
                    self.undoPlaceQueen(row, c)
        return count

    def isValid(self, row: int, c: int):
        for r_, c_ in self.placed:
            if c == c_ or c == c_ + (row - r_) or c == c_ - (row - r_):
                return False
        return True

    def placeQueen(self, row, c):
        self.placed.add((row, c))

    def undoPlaceQueen(self, row, c):
        self.placed.remove((row, c))


if __name__ == '__main__':
    x = Solution().totalNQueens(8)
    print(x)
