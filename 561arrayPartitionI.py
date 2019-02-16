import typing
class Solution:
    def arrayPairSum(self, nums: typing.List[int]) -> int:
        import itertools
        return sum(itertools.islice(sorted(nums), None, None, 2))
