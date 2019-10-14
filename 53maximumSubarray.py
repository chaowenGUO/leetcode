class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return max(itertools.accumulate(nums, lambda acc, num: max(acc + num, num)))
