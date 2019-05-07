class Solution:
    def getRow(self, rowIndex: int) -> 'List[int]':
        row = rowIndex + 1
        rst = [1] * row
        for r in range(1, row + 1):
            for c in range(1, r):
                num = 1 if c == r - 1 else rst[c - 1] + rst[c]
                temp = rst[r - 1]
                rst[r - 1] = num
                rst[c - 1] = temp
        return rst

    def getRow_reverse(self, rowIndex: int) -> 'List[int]':
        row = rowIndex + 1
        rst = [1] * row
        for r in range(1, row + 1):
            for c in range(r - 2, 0, -1):
                rst[c] += rst[c - 1]
        return rst


if __name__ == '__main__':
    x = Solution().getRow_reverse(-3)
    print(x)
