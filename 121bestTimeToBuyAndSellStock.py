class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        else:
            maxProfit, minPrice = 0, prices[0]
            for price in prices[1:]:
                maxProfit = max(maxProfit, price - minPrice)
                minPrice = min(minPrice, price)            
            return maxProfit
