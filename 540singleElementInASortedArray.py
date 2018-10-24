class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            middle = left + (right - left) // 2
            if nums[middle] == nums[middle ^ 1]: left = middle
            else: right = middle
        return nums[right] if nums[left] == nums[left - 1] else nums[left]
