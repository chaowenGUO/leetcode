# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

import typing
class Solution:
    def merge(self, intervals: typing.List[Interval]) -> typing.List[Interval]:
        result = []
        for interval in sorted(intervals, key = lambda _:_.start):
            if result and interval.start <= result[-1].end: result[-1].end = max(result[-1].end, interval.end)
            else: result += interval,
        return result
