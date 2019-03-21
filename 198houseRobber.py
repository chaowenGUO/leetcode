import functools

class Solution:
    def rob(self, nums: List[int]) -> int:
        return functools.reduce(lambda result, num: [result[1], max(result[1], result[0] + num)], nums, [0] * 2)[1]
