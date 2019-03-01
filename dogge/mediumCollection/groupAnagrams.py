class Solution:
    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
        dic = {}
        for s in strs:
            _ = ''.join(sorted(s))
            if dic.get(_) is None:
                dic[_] = [s]
            else:
                dic[_].append(s)
        return list(dic.values())


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
