import typing
class Solution:
    def kClosest(self, points: typing.List[typing.List[int]], K: int) -> typing.List[typing.List[int]]:
        import heapq
        return heapq.nsmallest(K, points, lambda distance: distance[0]**2 + distance[1]**2)
