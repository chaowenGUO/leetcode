import typing
class Solution:
    def maxProduct(self, nums: typing.List[int]) -> int:
        result = big = small = nums[0]
        for num in nums[1:]:
            big, small = (_(num, num * big, num * small) for _ in (max, min))
            result = max(result, big)
        return result
