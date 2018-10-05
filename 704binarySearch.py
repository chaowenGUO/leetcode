class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            middle = left + (right - left) // 2
            if nums[middle] < target: left = middle
            else: right = middle
        if nums[left] == target: return left
        elif nums[right] == target: return right
        else: return -1
