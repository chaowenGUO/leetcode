class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = big = small = nums[0]
        for num in nums[1:]:
            big, small=max(num, num * big, num * small), min(num, num * big, num * small)
            result = max(result, big)
        return result
