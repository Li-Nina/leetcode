#首先对所给的字符串列表（数组）进行排序，即对其中的每一个字符串都进行排序，这样就可以得到哪些字符串是归位一组的。
#接着将字符串列表转换为一个字典，并遍历key值得到最终的列表返回。
# class Solution(object):
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """
#         ans = []
#         temp_dict = {}
#         result = []
#         for word in strs:
#             ans.append("".join(sorted(word)))
#         for i in range(len(strs)):
#             if ans[i] not in temp_dict:
#                 temp_dict[ans[i]] = [strs[i]]
#             else:
#                 temp_dict[ans[i]].append(strs[i])
#         for key in temp_dict:
#             result.append(temp_dict[key])
#         return result
import collections
class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            b = sorted(s)
            c = tuple(b)
            ans[c].append(s)
        return ans.values()
c = ["eat", "tea", "tan", "ate", "nat", "bat"]
aa = Solution()
print(aa.groupAnagrams(c))

