class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        import functools, math, collections
        return functools.reduce(math.gcd, collections.Counter(deck).values()) > 1
