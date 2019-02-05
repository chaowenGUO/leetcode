import typing
class Solution:
    def missingNumber(self, nums: typing.List[int]) -> int:
        length = len(nums)
        return (length + 1) * length // 2 - sum(nums)
