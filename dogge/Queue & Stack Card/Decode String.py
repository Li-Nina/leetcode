class Solution:
    def decodeString(self, s: str) -> str:
        """
        s = "3[a]2[bc]", return "aaabcbc".
        s = "3[a2[c]]", return "accaccacc".
        s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
        """
        stack = []
        mini_stack = []

        for i in s:
            if i != ']':
                stack.append(i)
            else:
                _ = stack.pop()
                while _ != '[':
                    mini_stack.append(_)
                    _ = stack.pop()
                mini_s = ''.join(mini_stack[::-1])
                mini_stack.clear()

                while stack and stack[-1].isdigit():
                    mini_stack.append(stack.pop())
                mini_k = int(''.join(mini_stack[::-1]))
                mini_stack.clear()

                stack.append(mini_k * mini_s)
        return ''.join(stack)


if __name__ == '__main__':
    x = Solution().decodeString('2[abc]3[cd]ef')
    print(x)
