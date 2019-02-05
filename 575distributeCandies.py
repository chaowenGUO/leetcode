import typing
class Solution:
    def distributeCandies(self, candies: typing.List[int]) -> int:
        return min(len(candies) // 2, len({*candies}))
