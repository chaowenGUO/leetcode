class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        return min(len({*candies}), len(candies) // 2)
