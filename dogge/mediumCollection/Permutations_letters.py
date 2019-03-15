class Solution:
    def permutations_letter(self, letters):
        rst = []

        def backtracking(prefix, suffix):
            if not suffix:
                rst.append(prefix)
            else:
                for i in range(len(suffix)):
                    backtracking(prefix + suffix[i], suffix[0:i] + suffix[i + 1:])

        backtracking("", letters)
        return rst


if __name__ == '__main__':
    x = Solution().permutations_letter("abc")
    print(x)
