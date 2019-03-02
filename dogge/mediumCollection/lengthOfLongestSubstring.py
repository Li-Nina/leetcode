class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _dic = {}
        _queue = []
        max_length = 0
        length = 0
        for i in s:
            if _dic.get(i):
                while _queue and _queue[0] != i:
                    f = _queue.pop(0)
                    _dic[f] = _dic[f] - 1
                    length -= 1
                    max_length = length if length > max_length else max_length
                _queue.pop(0)
                _queue.append(i)
            else:
                _dic[i] = 1 if _dic.get(i) is None else _dic[i] + 1
                _queue.append(i)
                length += 1
                max_length = length if length > max_length else max_length
        return max_length


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("aabaab!bb"))
