import typing
class Solution:
    def smallestRangeI(self, A: typing.List[int], K: int) -> int:
        return max(0, max(A) - min(A) - 2 * K)
