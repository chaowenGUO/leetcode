class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = [0, *itertools.accumulate(nums)]
        return max(map(operator.sub, itertools.islice(sums, k, None), sums)) / k
