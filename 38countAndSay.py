class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        import collections
        result = '1'
        for _ in range(n - 1): result = ''.join(str(len(list(group))) + key for key, group in itertools.groupby(result))
        return result
