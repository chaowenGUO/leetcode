import functools

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return functools.reduce(lambda result, num: [*result, *([*_, num] for _ in result)], nums, [[]])
