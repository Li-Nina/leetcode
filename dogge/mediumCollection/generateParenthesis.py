class Solution:
    def generateParenthesis(self, n: int) -> 'List[str]':
        def dfsHelper(combination, lbracket_left, rbracket_left):
            if lbracket_left == 0 and rbracket_left == 0:
                rst.append(combination)
            elif lbracket_left == 0 and rbracket_left > 0:
                dfsHelper(combination + ")", lbracket_left, rbracket_left - 1)
            elif lbracket_left < rbracket_left:
                dfsHelper(combination + "(", lbracket_left - 1, rbracket_left)
                dfsHelper(combination + ")", lbracket_left, rbracket_left - 1)
            else:
                dfsHelper(combination + "(", lbracket_left - 1, rbracket_left)

        rst = []
        dfsHelper("", n, n)
        return rst


if __name__ == '__main__':
    x = Solution().generateParenthesis(4)
    print(x)
