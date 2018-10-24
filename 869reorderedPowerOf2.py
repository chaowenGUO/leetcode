class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        import collections
        return any(collections.Counter(str(N)) == collections.Counter(str(1 << _)) for _ in range(31))
