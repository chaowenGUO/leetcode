import typing
class Solution:
    def isValidSudoku(self, board: typing.List[typing.List[str]]) -> bool:
        seen = []
        for i, row in enumerate(board):
            for j, column in enumerate(row):
                if column != '.': seen += [(column, j), (i, column), (i // 3, j // 3, column)]
        return len(seen) == len({*seen})
