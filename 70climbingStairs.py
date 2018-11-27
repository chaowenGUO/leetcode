class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        import functools
        return functools.reduce(lambda result, _: [result[1], sum(result)], range(n), [1] * 2)[0]
