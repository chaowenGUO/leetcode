import typing
class Solution:
    def permuteUnique(self, nums: typing.List[int]) -> typing.List[typing.List[int]]:
        import functools
        return functools.reduce(lambda result, num: [permutation[:_] + [num] + permutation[_:] for permutation in result for _ in range((permutation + [num]).index(num) + 1)], nums, [[]])
