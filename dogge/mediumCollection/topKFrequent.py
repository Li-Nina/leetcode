import collections
import heapq


class Solution:
    def topKFrequent(self, nums: 'List[int]', k: int) -> 'List[int]':
        num_dict = collections.Counter(nums)
        return heapq.nlargest(k, num_dict, key=num_dict.get)


if __name__ == '__main__':
    # count = collections.Counter([1, 2, 3, 4, 1, 1, 1, 2, 3, 4, 5])
    # x = heapq.nlargest(2, count.keys(), key=count.get)
    # print(x)
    dic = {'a': 9, 'b': 8, 'c': 0, 'd': -2, 'e': 2}
    x = heapq.nsmallest(2, dic.keys(), dic.get)
    print(x)
