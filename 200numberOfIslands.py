class Solution:
    def sink(self, grid, row, column):
            if 0 <= row < len(grid) and 0 <= column < len(grid[row]) and grid[row][column] == '1':
                grid[row][column] = '0'
                for _ in map(self.sink, (grid,) * 4, (row + 1, row - 1, row, row), (column, column, column + 1, column - 1)): pass
                return 1
            return 0
        
    def numIslands(self, grid: List[List[str]]) -> int:     
        return sum(self.sink(grid, row, column) for row in range(len(grid)) for column in range(len(grid[row])))
