import math


class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i * i for i in range(1, math.floor(math.sqrt(n)) + 1)]
        queue = [n]
        rst = -1
        visited = {n}
        while queue:
            rst += 1
            length = len(queue)
            for _ in range(length):
                x = queue.pop(0)
                if x == 0:
                    return rst
                for i in squares:
                    if x - i >= 0 and x - i not in visited:
                        queue.append(x - i)
                        visited.add(x - i)
        return -1


if __name__ == '__main__':
    print(Solution().numSquares(7168))
