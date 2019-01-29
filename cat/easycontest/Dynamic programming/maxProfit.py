# class Solution:
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if len(prices)==0:
#             return 0
#         minPrice = prices[0]
#         maxprofit = [0]*len(prices)
#         for i in range(0, len(prices)):
#             minPrice = min(minPrice,prices[i])
#             maxprofit[i] = max(maxprofit[i-1], prices[i]-minPrice)
#         return maxprofit[-1]
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        minPrice = prices[0]
        maxprofit = 0
        for p in prices:
            if p<minPrice:
                minPrice = p
            elif (p-minPrice)>maxprofit:
                maxprofit = p-minPrice
        return maxprofit
prices_1 = [3,2,4,5,2,7,1,4]
aa = Solution()
print(aa.maxProfit(prices_1))

