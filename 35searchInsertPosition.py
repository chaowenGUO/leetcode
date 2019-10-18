class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            middle = left + (right - left) // 2
            if nums[middle] < target: left = middle + 1
            else: right = middle
        return left
