class Solution:
    def openLock(self, deadends: 'List[str]', target: str) -> int:
        def enqueue(s):
            for i in range(4):
                add(s[0:i] + str((int(s[i]) + 1) % 10) + s[i + 1:])
                add(s[0:i] + str((int(s[i]) - 1) % 10) + s[i + 1:])

        def add(s):
            if s not in visited and s not in deadends:
                queue.append(s)
                visited.add(s)

        here = '0000'
        if here == target:
            return 0
        if here not in deadends:
            rst = -1
            visited = {here}
            queue = [here]
            while queue:
                length = len(queue)
                rst += 1
                for _ in range(length):
                    here = queue.pop(0)
                    if here == target:
                        return rst
                    enqueue(here)
        return -1


if __name__ == '__main__':
    x = Solution().openLock(deadends=["0201", "0101", "0102", "1212", "2002"], target="0202")
    print(x)
    x = Solution().openLock(deadends=["8888"], target="0009")
    print(x)
    x = Solution().openLock(deadends=["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], target="8888")
    print(x)
    x = Solution().openLock(deadends=["0000"], target="8888")
    print(x)
