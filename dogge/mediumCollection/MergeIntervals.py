# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '[{} {}]'.format(self.start, self.end)


class Solution:
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        intervals.sort(key=lambda x: x.start)
        rst = []
        for interval in intervals:
            if not rst or interval.start > rst[-1].end:
                rst.append(interval)
            elif interval.end > rst[-1].end:
                rst[-1].end = interval.end
        return rst


if __name__ == '__main__':
    i = []
    i.append(Interval(0, 1))
    i.append(Interval(2, 6))
    i.append(Interval(8, 9))
    i.append(Interval(6, 9))
    i.append(Interval(1, 4))
    i.append(Interval(0, 8))
    i.append(Interval(6, 7))
    i.append(Interval(5, 15))
    print(' '.join(map(str, i)))

    o = Solution().merge(i)
    print(' '.join(map(str, o)))
