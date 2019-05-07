class Solution:
    # todo
    def reorganizeString(self, S: str) -> str:
        rst = []
        waiting = {}
        for s in S:
            if not rst or rst[-1] != s:
                rst.append(s)
            else:
                waiting[s] = waiting.get(s, 0) + 1
                for k, v in waiting.items():
                    if k != rst[-1] and v != 0:
                        rst.append(k)
                        if v - 1 != 0:
                            waiting[k] = v - 1
                        else:
                            waiting.pop(k)
                        break
        if waiting:
            item = waiting.popitem()
            if waiting or item[1] > 1 or (item[0] == rst[0] and item[0] == rst[-1]):
                return ""
            else:
                if item[0] != rst[-1]:
                    rst.append(item[0])
                    return ''.join(rst)
                else:
                    return item[0] + ''.join(rst)
        else:
            return ''.join(rst)


if __name__ == '__main__':
    x = Solution().reorganizeString("vvvlo")
    print(x)
