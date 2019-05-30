class Solution:
    def generateParenthesis_recursion(self, n: int) -> 'List[str]':
        rst = []

        def backtracking(track: 'List[str]', lnum: int, rnum: int):
            if lnum == rnum == n:
                rst.append(''.join(track))
            elif lnum >= rnum:
                if lnum == n:
                    track.append(')')
                    backtracking(track, lnum, rnum + 1)
                    track.pop()
                else:
                    track.append('(')
                    backtracking(track, lnum + 1, rnum)
                    track.pop()
                    track.append(')')
                    backtracking(track, lnum, rnum + 1)
                    track.pop()

        backtracking([], 0, 0)
        return rst

    def generateParenthesis_iteration(self, n: int) -> 'List[str]':
        pass


if __name__ == '__main__':
    x = Solution().generateParenthesis_recursion(10)
    print(x)
