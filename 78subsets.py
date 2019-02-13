import typing
class Solution:
    def subsets(self, nums: typing.List[int]) -> typing.List[typing.List[int]]:
        import functools
        return functools.reduce(lambda result, num: result + [_ + [num] for _ in result], nums, [[]])
