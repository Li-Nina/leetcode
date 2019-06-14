class Solution:
    """
    @param n: The number of digits
    @return: All narcissistic numbers with n digits
    """

    def getNarcissisticNumbers(self, n):
        # write your code here
        r = []
        for i in range(10 ** (n - 1), 10 ** n):
            rst = 0
            for _ in range(n):
                rst += (i // (10 ** _) % 10) ** n
            if rst == i:
                r.append(i)
        if n == 1:
            r.insert(0, 0)
        return r
