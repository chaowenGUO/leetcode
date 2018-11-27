class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        import itertools, functools
        return functools.reduce(lambda result, _: ''.join(str(len([*group])) + key for key, group in itertools.groupby(result)), range(n - 1), '1')
