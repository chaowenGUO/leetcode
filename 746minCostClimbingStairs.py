class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        import functools
        return min(functools.reduce(lambda result, _: [result[1], min(result) + _], cost, [0] * 2))
