class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lens_str = []
        res = ""
        if strs:
            for i in strs:
                if i:
                    lens_str.append(len(i))
                else:
                    return ""
            len_min = min(lens_str)
            for i in range(len_min):
                for j in range(1, len(strs)):
                    if strs[j][i]!= strs[0][i]:
                        return res
                res += strs[0][i]
            return res
        else:
            return ""
    def longestCommonPrefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = []
        for x in zip(*strs):#zip函数接受任意多个（包括0个和1个）序列作为参数，返回一个tuple列表。具体意思不好用文字来表述，直接看示例：
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break
        return "".join(prefix)
    #在函数调用中使用 * list / tuple的方式表示将list / tuple分开，作为位置参数传递给对应函数（前提是对应函数支持不定个数的位置参数）
a = ["dog","docecar","dar"]
print(Solution().longestCommonPrefix2(a))

