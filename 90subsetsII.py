import functools

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        return functools.reduce(lambda result, num: result + [_ + [num] for _ in result if _ + [num] not in result], sorted(nums), [[]])
