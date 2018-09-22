import collections


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1 = set()
        s2 = set()
        for i in s:
            if i not in s1 and i not in s2:
                s1.add(i)
            elif i not in s1 and i in s2:
                continue
            else:
                s1.remove(i)
                s2.add(i)
        if len(s1) > 0:
            for i, v in enumerate(s):
                if v in s1:
                    return i
        else:
            return -1
            #
            # alpha = collections.defaultdict(int)
            # for i in s:
            #     alpha[i]+=1
            # for j, v in enumerate(s):
            #     if alpha[v] ==1:
            #         return j
            # return -1


a = "loveleetvcod"
print(Solution().firstUniqChar(a))
