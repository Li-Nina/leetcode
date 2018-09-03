class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        j = 0
        profit = 0
        buy = None
        sell = None
        for i, v in enumerate(prices[:-1]):
            j += 1
            if buy is None and prices[j] > v:
                buy = v
            if buy is not None:
                if prices[j] < v:
                    sell = v
                    profit = profit + sell - buy
                    buy = None
                    sell = None
                if sell is None and buy is not None and j == len(prices) - 1:
                    sell = prices[j]
                    profit = profit + sell - buy
                    buy = None

        return profit