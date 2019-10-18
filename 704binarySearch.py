class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = bisect.bisect_left(nums, target)
        return left if target in nums[left:left + 1] else -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            middle = left + (right - left) // 2
            if nums[middle] < target: left = middle + 1
            else: right = middle
        return left if target in nums[left:left + 1] else -1
