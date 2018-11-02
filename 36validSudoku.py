class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = []
        for i, row in enumerate(board):
            for j, column in enumerate(row):
                if column != '.': seen += [(column, j), (i, column), (i // 3, j // 3, column)]
        return len(seen) == len({*seen})
