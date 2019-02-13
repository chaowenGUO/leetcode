import typing
class Solution:
    def hasGroupsSizeX(self, deck: typing.List[int]) -> bool:
        import functools, math, collections
        return functools.reduce(math.gcd, collections.Counter(deck).values()) > 1
