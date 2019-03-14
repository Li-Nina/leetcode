class Solution:
    """
    DFS approach
    """

    def numIslands(self, grid: 'List[List[str]]') -> int:
        rst = 0
        if grid:
            row_num = len(grid)
            column_num = len(grid[0])
            for r in range(row_num):
                for c in range(column_num):
                    if grid[r][c] == '1':
                        rst += 1
                        self.helper(grid, r, c, row_num, column_num)
        return rst

    def helper(self, grid, r, c, row_num, column_num):
        if (r >= row_num or r < 0) or (c >= column_num or c < 0) or grid[r][c] == '0':
            return
        else:
            grid[r][c] = '0'
            self.helper(grid, r + 1, c, row_num, column_num)
            self.helper(grid, r, c + 1, row_num, column_num)
            self.helper(grid, r - 1, c, row_num, column_num)
            self.helper(grid, r, c - 1, row_num, column_num)
