class Solution:
    def lower(self, nums, target):
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            middle = left + (right - left) // 2
            if nums[middle] < target: left = middle
            else: right = middle
        if nums[left] == target: return left
        elif nums[right] == target: return right
        else: return -1
        
    def upper(self, nums, target):
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            middle = left + (right - left) // 2
            if nums[middle] <= target: left = middle
            else: right = middle
        if nums[right] == target: return right
        elif nums[left] == target: return left
        else: return -1
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [_(nums, target) for _ in (self.lower, self.upper)] if nums else [-1] * 2
