class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        return [left, bisect.bisect(nums, target) - 1] if target in itertools.islice(nums, left, left + 1) else [-1] * 2
