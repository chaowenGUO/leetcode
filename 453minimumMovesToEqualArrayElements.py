import typing
class Solution:
    def minMoves(self, nums: typing.List[int]) -> int:
        return sum(nums) - len(nums) * min(nums)
