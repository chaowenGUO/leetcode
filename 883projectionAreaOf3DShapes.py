class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        return sum(map(max, grid)) + sum(map(max, zip(*grid))) + sum(_ > 0 for row in grid for _ in row)
