import typing
class Solution:
    def sink(self, grid: typing.List[typing.List[str]], row: int, column: int) -> None:
        if 0 <= row < len(grid) and 0 <= column < len(grid[0]) and grid[row][column] == '1':
            grid[row][column] = '0'
            self.sink(grid, row + 1, column)
            self.sink(grid, row - 1, column)
            self.sink(grid, row, column + 1)
            self.sink(grid, row, column - 1)
        
    def numIslands(self, grid: typing.List[typing.List[str]]) -> int:
        result = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == '1':
                    self.sink(grid, row, column)
                    result += 1
        return result
