class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        for index, num in enumerate(nums):
            if index <= reach: reach = max(reach, index + num)
        return reach >= len(nums) - 1
