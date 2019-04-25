class Solution:
    def numIslands_BFS(self, grid: 'List[List[str]]') -> int:
        rst = 0
        if grid and grid[0]:
            queue = []
            visited = set()
            row = len(grid)
            col = len(grid[0])

            def queue_oper():
                while queue:
                    m, n = queue.pop(0)
                    grid[m][n] = '0'
                    if (m + 1, n) not in visited and m + 1 < row and grid[m + 1][n] == '1':
                        queue.append((m + 1, n))
                        visited.add((m + 1, n))
                    if (m, n + 1) not in visited and n + 1 < col and grid[m][n + 1] == '1':
                        queue.append((m, n + 1))
                        visited.add((m, n + 1))
                    if (m - 1, n) not in visited and m - 1 >= 0 and grid[m - 1][n] == '1':
                        queue.append((m - 1, n))
                        visited.add((m - 1, n))
                    if (m, n - 1) not in visited and n - 1 >= 0 and grid[m][n - 1] == '1':
                        queue.append((m, n - 1))
                        visited.add((m, n - 1))

            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == '1':
                        rst += 1
                        queue.append((i, j))
                        visited.add((i, j))
                        queue_oper()
        return rst

    def numIslands_DFS(self, grid: 'List[List[str]]') -> int:
        rst = 0
        if grid and grid[0]:
            stack = []
            visited = set()
            row = len(grid)
            col = len(grid[0])

            def queue_oper():
                while stack:
                    m, n = stack.pop()
                    grid[m][n] = '0'
                    if (m + 1, n) not in visited and m + 1 < row and grid[m + 1][n] == '1':
                        stack.append((m + 1, n))
                        visited.add((m + 1, n))
                    if (m, n + 1) not in visited and n + 1 < col and grid[m][n + 1] == '1':
                        stack.append((m, n + 1))
                        visited.add((m, n + 1))
                    if (m - 1, n) not in visited and m - 1 >= 0 and grid[m - 1][n] == '1':
                        stack.append((m - 1, n))
                        visited.add((m - 1, n))
                    if (m, n - 1) not in visited and n - 1 >= 0 and grid[m][n - 1] == '1':
                        stack.append((m, n - 1))
                        visited.add((m, n - 1))

            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == '1':
                        rst += 1
                        stack.append((i, j))
                        visited.add((i, j))
                        queue_oper()
        return rst
