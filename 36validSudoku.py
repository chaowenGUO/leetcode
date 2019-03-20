class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = ([(column, j), (i, column), (i // 3, j // 3, column)] for i, row in enumerate(board) for j, column in enumerate(row) if column != '.')
        seen = *itertools.chain(*seen),
        return len(seen) == len({*seen})
