import typing
class Solution:
    def singleNumber(self, nums: typing.List[int]) -> int:
        import functools, operator
        return functools.reduce(operator.xor, nums)
