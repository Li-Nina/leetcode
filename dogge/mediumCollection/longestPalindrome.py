class Solution:
    def longestPalindrome_origin(self, s: str) -> str:
        length = len(s)
        dp = {}
        max_len = 1
        start = 0

        for _len in range(2, length + 1):
            i = 0
            while i <= length - _len:
                j = i + _len - 1
                if _len <= 3:
                    dp[(i, j)] = s[i] == s[j]
                elif s[i] == s[j]:
                    dp[(i, j)] = dp[(i + 1, j - 1)]
                else:
                    dp[(i, j)] = False

                if dp[(i, j)] and _len > max_len:
                    max_len = _len
                    start = i
                i += 1

        return s[start:start + max_len]

    def longestPalindrome2(self, s: str) -> str:
        length = len(s)
        dp = {}
        max_len = 1
        start = 0

        for _len in range(2, length + 1):
            i = 0
            while i <= length - _len:
                j = i + _len - 1
                if _len <= 3 and s[i] == s[j]:
                    dp[(i, j)] = True
                    if _len > max_len:
                        max_len = _len
                        start = i
                elif s[i] == s[j] and dp.get((i + 1, j - 1)):
                    dp[(i, j)] = True
                    if _len > max_len:
                        max_len = _len
                        start = i
                i += 1
        return s[start:start + max_len]

    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        dp = {}
        max_len = 1
        start = 0

        for _len in range(2, length + 1):
            i = 0
            while i <= length - _len:
                j = i + _len - 1
                if (_len <= 3 and s[i] == s[j]) or (s[i] == s[j] and dp.get((i + 1, j - 1))):
                    dp[(i, j)] = True
                    if _len > max_len:
                        max_len = _len
                        start = i
                i += 1
        return s[start:start + max_len]


if __name__ == '__main__':
    s = "abcda"
    x = Solution().longestPalindrome(s)
    print(x)
