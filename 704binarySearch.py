class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = bisect.bisect_left(nums, target)
        return left if target in itertools.islice(nums, left, left + 1) else -1
