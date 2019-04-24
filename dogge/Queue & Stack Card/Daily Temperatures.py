class Solution:
    def dailyTemperatures(self, T: 'List[int]') -> 'List[int]':
        if not T:
            return []
        rst = [0 for _ in range(len(T))]
        stack = [T[0]]
        low = T[0]

        for i in range(1, len(T)):
            if T[i] <= low:
                stack.append(T[i])
                low = T[i]
            else:
                count = 1
                while stack:
                    stack.pop()
                    if rst[i - count] == 0:
                        rst[i - count] = count
                    count += 1
                stack.append(T[i])
                low = T[i]
        return rst


if __name__ == '__main__':
    x = Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    print(x)
