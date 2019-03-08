class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            middle = left + (right - left) // 2
            if nums[middle] < target: left = middle
            else: right = middle
        if nums[left] >= target: return left
        elif nums[right] >= target: return right
        else: return len(nums)
