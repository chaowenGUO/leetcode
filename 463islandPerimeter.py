class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 1:
                    result += 4
                    if row > 0 and grid[row - 1][column] == 1: result -= 2
                    if column > 0 and grid[row][column - 1] == 1: result -= 2
        return result
