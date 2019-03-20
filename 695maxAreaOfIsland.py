class Solution:
    def sink(self, grid, row, column):
        if 0 <= row < len(grid) and 0 <= column < len(grid[row]) and grid[row][column]:
            grid[row][column] = 0
            return 1 + sum(map(self.sink, (grid,) * 4, (row + 1, row - 1, row, row), (column, column, column + 1, column - 1)))
        else: return 0
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        return max(self.sink(grid, row, column) for row in range(len(grid)) for column in range(len(grid[row])))
