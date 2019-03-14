# #一次遍历时，使用字典保存每个字符第一次出现的位置。这个方法我一直不知道叫什么名字，就勉强叫做prefix方法吧，因为需要维护已经遍历到的前缀部分。
#
# 当right向后遍历的过程中，如果这个字符在字典中，说明这个字符在前面出现过，即这个区间已经不是题目要求的不含重复字符的区间了，因此，需要移动left。
#
# 移动left到哪里呢？有个快速的方法，那就是移动到right字符在字典中出现的位置（即s[right]在前面的位置）的下一个位置。
#
# 无论如何都会使用right更新字典，另外记录最大区间长度即为所求。
#
# 注意，left更新的时候需要保留最大（最右）的位置。举例说明：
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = right =0
        chars_dict = dict()
        res = 0
        for right in range(len(s)):
            if s[right] in chars_dict:
                left = max(left, chars_dict[s[right]]+1)
            chars_dict[s[right]]=right
            res = max(res, right-left+1)
        return res