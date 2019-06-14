"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def canAttendMeetings(self, intervals):
        # Write your code here
        s = []
        for _ in intervals:
            for i in s:
                if not i.start < _.start < _.end < i.end:
                    return False
            s.append(_)
        return True


if __name__ == '__main__':
    t = Solution().canAttendMeetings([Interval(465, 497),
                                      Interval(386, 462),
                                      Interval(354, 380),
                                      Interval(134, 189),
                                      Interval(199, 282),
                                      Interval(18, 104),
                                      Interval(499, 562),
                                      Interval(4, 14),
                                      Interval(111, 129),
                                      Interval(292, 345),
                                      ])
    print(t)
