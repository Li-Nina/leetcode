class Solution:
    def evalRPN(self, tokens: 'List[str]') -> int:
        def evals(x, y, oper):
            if oper == '+':
                return y + x
            elif oper == '-':
                return y - x
            elif oper == '*':
                return y * x
            else:
                return y / x

        stack = []
        opers = {'+', '-', '*', '/'}
        for token in tokens:
            if token in opers:
                stack.append(int(evals(stack.pop(), stack.pop(), token)))
            else:
                stack.append(int(token))
        return stack.pop()

    def evalRPN_fancy_lamda(self, tokens: 'List[str]') -> int:
        opers_dic = {
            '+': lambda x, y: y + x,
            '-': lambda x, y: y - x,
            '*': lambda x, y: y * x,
            '/': lambda x, y: y / x
        }

        stack = []
        for token in tokens:
            if token in opers_dic:
                stack.append(int(opers_dic[token](stack.pop(), stack.pop())))
            else:
                stack.append(int(token))
        return stack.pop()


if __name__ == '__main__':
    r = Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
    print(r)
    r = Solution().evalRPN_fancy_lamda(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
    print(r)
    g = lambda a, b, c: a + b + c
    print(g(1, 2, 3))
