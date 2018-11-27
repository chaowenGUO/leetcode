class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        import functools
        return functools.reduce(lambda result, _:[[_] + combination for combination in result for _ in range(1, combination[0] if combination else n + 1)], range(k), [[]])
