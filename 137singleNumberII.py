import typing
class Solution:
    def singleNumber(self, nums: typing.List[int) -> int:
        a = b = 0
        for num in nums:
            a = (a ^ num) | b
            b = (b ^ num) & a
        return b
