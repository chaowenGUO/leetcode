import functools

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return functools.reduce(lambda result, num: [[*permutation[:_], num, *permutation[_:]] for permutation in result for _ in range([*permutation, num].index(num) + 1)], nums, [[]])
