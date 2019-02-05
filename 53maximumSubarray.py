import typing
class Solution:
    def maxSubArray(self, nums: typing.List[int]) -> int:
        result = big = nums[0]
        for num in nums[1:]:
            big = max(num, num + big)
            result = max(result, big)
        return result
