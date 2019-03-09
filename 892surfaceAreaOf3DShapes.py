class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        return sum(_ * 4 + 2 for row in grid for _ in row if _) - sum(min(_) * 2 for row in itertools.chain(grid, zip(*grid)) for _ in zip(row, itertools.islice(row, 1, None)))
