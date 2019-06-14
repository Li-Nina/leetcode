class Solution:
    """
    @param A: An integer array
    @return: An integer
    """

    def singleNumber(self, A):
        # write your code here
        s = set()
        for i in A:
            if i in s:
                s.remove(i)
            else:
                s.add(i)
        return s.pop()
