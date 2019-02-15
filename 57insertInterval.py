# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

import typing
class Solution:
    def insert(self, intervals: typing.List[Interval], newInterval: Interval) -> typing.List[Interval]:
        start, end = newInterval.start, newInterval.end
        left = [_ for _ in intervals if _.end < start]
        right = [_ for _ in intervals if _.start > end]
        if left + right != intervals:
            start = min(start, intervals[len(left)].start)
            end = max(end, intervals[~len(right)].end)
        return [*left, Interval(start, end), *right]
