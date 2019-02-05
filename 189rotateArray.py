import typing
class Solution:
    def rotate(self, nums: typing.List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - k
        nums[:] = nums[n:] + nums[:n]
