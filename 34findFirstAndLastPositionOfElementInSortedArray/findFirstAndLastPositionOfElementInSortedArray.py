class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = (_(nums, target) for _ in (bisect.bisect_left, bisect.bisect))
        return [left, right - 1] if left != right else [-1] * 2
