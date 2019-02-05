import typing
class Solution:
    def minPathSum(self, grid: typing.List[typing.List[int]]) -> int:
        *grid[0], = itertools.accumulate(grid[0])
        for row in range(1, len(grid)): grid[row][0] += grid[row - 1][0]
        for row in range(1, len(grid)):
            for column in range(1, len(grid[0])): grid[row][column] += min(grid[row - 1][column], grid[row][column - 1])
        return grid[-1][-1]
