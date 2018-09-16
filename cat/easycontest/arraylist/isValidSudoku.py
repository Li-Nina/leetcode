class Solution:
    def isValid(self, list_num):
        s = set()
        for i in list_num:
            if i is not ".":
                if i in s:
                    return False
                else:
                    s.add(i)
        s.clear()

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for rows in board:
            if self.isValid(rows)==False:
                return False
        i = 0
        while i < 9:
            cols = [x[i] for x in board]
            if self.isValid(cols)==False:
                return False
            i += 1
        for a in [0, 3, 6]:
            for b in [0, 3, 6]:
                block = [board[s][t] for s in [a, a + 1, a + 2] for t in [b, b + 1, b + 2]]
                if self.isValid(block) == False:
                    return False
        return True


gougou = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
print(Solution().isValidSudoku(gougou))
