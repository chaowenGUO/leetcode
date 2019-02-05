import typing
class Solution:
    def rob(self, nums: typing.List[int]) -> int:
        import functools
        return functools.reduce(lambda result, num: [result[1], max(result[1], num + result[0])], nums, [0] * 2)[1]
