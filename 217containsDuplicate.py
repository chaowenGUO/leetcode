import typing
class Solution:
    def containsDuplicate(self, nums: typing.List[int]) -> bool:
        return len(nums) != len({*nums})
