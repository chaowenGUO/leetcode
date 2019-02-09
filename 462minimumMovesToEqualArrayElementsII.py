import typing
class Solution:
    def minMoves2(self, nums: typing.List[int]) -> int:
        nums = sorted(nums)
        return sum(nums[~_] - nums[_] for _ in range(len(nums) // 2))
