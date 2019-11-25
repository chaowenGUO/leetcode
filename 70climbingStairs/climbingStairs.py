import functools

class Solution:
    def climbStairs(self, n: int) -> int:
        return functools.reduce(lambda result, _: [result[1], sum(result)], range(n), [1] * 2)[0]
