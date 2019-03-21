import functools

class Solution:
    def line(self, nums):
        return functools.reduce(lambda result, num: [result[1], max(result[1], result[0] + num)], nums, [0] * 2)[1]
    
    def rob(self, nums: List[int]) -> int:
        return max(map(self.line, (nums[len(nums) != 1:], nums[:-1])))
