class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        import functools, itertools
        return functools.reduce(lambda result, _: ''.join(str(sum(1 for _ in group)) + key for key, group in itertools.groupby(result)), range(n - 1), '1')
