class Solution:
    def floodFill(self, image: 'List[List[int]]', sr: int, sc: int, newColor: int) -> 'List[List[int]]':
        old_color = image[sr][sc]
        if old_color == newColor:
            return image
        row_num = len(image)
        col_num = len(image[0])

        stack = [(sr, sc)]
        visited = {(sr, sc)}
        while stack:
            r, c = stack.pop()
            if 0 <= r < row_num and 0 <= c < col_num and image[r][c] == old_color:
                image[r][c] = newColor
                if (r - 1, c) not in visited:
                    stack.append((r - 1, c))
                    visited.add((r - 1, c))
                if (r + 1, c) not in visited:
                    stack.append((r + 1, c))
                    visited.add((r + 1, c))
                if (r, c - 1) not in visited:
                    stack.append((r, c - 1))
                    visited.add((r, c - 1))
                if (r, c + 1) not in visited:
                    stack.append((r, c + 1))
                    visited.add((r, c + 1))
        return image
