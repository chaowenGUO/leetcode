import functools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return functools.reduce(lambda result, num: [[*permutation[:_], num, *permutation[_:]] for permutation in result for _ in range(len(permutation) + 1)], nums, [[]])
