class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def bfsHelper(string_builder, next_digit_index):
            if next_digit_index == len(digits):
                return rst.append(string_builder)
            for letter in phone[digits[next_digit_index]]:
                bfsHelper(string_builder + letter, next_digit_index + 1)

        rst = []
        if digits:
            bfsHelper("", 0)
        return rst


if __name__ == '__main__':
    x = Solution().letterCombinations('23')
    print(x)
