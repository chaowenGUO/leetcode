class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        for interval in sorted(intervals, key = lambda _:_[0]):
            if result and interval[0] <= result[-1][1]: result[-1][1] = max(result[-1][1], interval[1])
            else: result += interval,
        return result
