class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = big = nums[0]
        for num in nums[1:]:
            big = max(num, big + num)
            result = max(big, result)
        return result
