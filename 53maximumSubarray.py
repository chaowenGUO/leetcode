class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = dp = nums[0]
        for num in nums[1:]:
            dp = max(dp + num, num)
            result = max(result, dp)
        return result
