class Solution:
    def canVisitAllRooms(self, rooms: 'List[List[int]]') -> bool:
        stack = [0]
        seen = [False] * len(rooms)
        seen[0] = True

        while stack:
            keys = rooms[stack.pop()]
            for k in keys:
                if not seen[k]:
                    stack.append(k)
                    seen[k] = True

        return all(seen)


if __name__ == '__main__':
    x = Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]])
    print(x)
