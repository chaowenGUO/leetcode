class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(max(prices[_ + 1] - prices[_], 0) for _ in range(len(prices) - 1))
