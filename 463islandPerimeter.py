class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        return sum(sum(map(operator.ne, itertools.chain([0], row), itertools.chain(row, [0]))) for row in itertools.chain(grid, map(list, zip(*grid))))
