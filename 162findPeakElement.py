class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            middle = left + (right - left) // 2
            if nums[middle] < nums[middle + 1]: left = middle
            else: right = middle
        return left if nums[left] > nums[right] else right
