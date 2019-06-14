import collections
import re


class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """

    def rotateString(self, s, offset):
        # write your code here
        if s:
            offset = offset % len(s) if offset > len(s) else offset
            t = s[(len(s) - offset):] + s[0:(len(s) - offset)]
            s.clear()
            s.extend(t)

    def firstUniqChar(str):
        # Write your code here
        s = collections.OrderedDict()
        for _ in str:
            s[_] = s.get(_, 0) + 1
        for k, v in s.items():
            if v == 1:
                return k

    def reverseWords(self, s):
        # write your code here
        t = s.strip().split(' ')
        t.reverse()
        t = [_ for _ in t if _]
        return ' '.join(t)

    def strStr(self, source, target):
        for i in range(len(source)):
            if source[i:len(target) + i] == target:
                return i
        return -1 if target else 0

    def mostFrequentlyAppearingLetters(self, str):
        # Write your code here.
        s = {}
        rst = 0
        for _ in str:
            s[_] = s.get(_, 0) + 1
        for k, v in s.items():
            if rst < v:
                rst = v
        return rst


if __name__ == '__main__':
    t = Solution().mostFrequentlyAppearingLetters("sdfsdf")
    print(t)
