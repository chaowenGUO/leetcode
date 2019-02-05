import typing
class Solution:
    def permute(self, nums: typing.List[int]) -> typing.List[typing.List[int]]:
        import functools
        return functools.reduce(lambda result, num: [permutation[:_] + [num] + permutation[_:] for permutation in result for _ in range(len(permutation) + 1)], nums, [[]])
