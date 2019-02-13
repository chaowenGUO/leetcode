import typing
class Solution:
    def isValidSudoku(self, board: typing.List[typing.List[str]]) -> bool:
        import itertools
        *seen, = itertools.chain(*([(column, j), (i, column), (i // 3, j // 3, column)] for i, row in enumerate(board) for j, column in enumerate(row) if column != '.'))
        return len(seen) == len({*seen})
