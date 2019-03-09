import functools

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(functools.reduce(lambda result, _: [result[1], min(result) + _], cost, [0] * 2))
