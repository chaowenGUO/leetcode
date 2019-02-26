class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(itertools.islice(sorted(nums), None, None, 2))
