import typing
class Solution:
    import string
    def dfs(self, board: typing.List[typing.List[str]], stack: typing.List[typing.Tuple[int, int]]) -> None:
        if not stack: return
        x, y = stack.pop()
        box = [board[x // 3 * 3 + i][y // 3 * 3 + j] for i in range(3) for j in range(3)]
        row = [board[_][y] for _ in range(9)]
        column = [board[x][_] for _ in range(9)]
        for _ in string.digits[1:]:
            if not any([_ in box, _ in row, _ in column]):
                board[x][y] = _
                self.dfs(board, stack)
                if not stack: return
        board[x][y] = '.'
        stack += (x, y),
        
    def solveSudoku(self, board: typing.List[typing.List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        stack = [(row, column) for row in range(9) for column in range(9) if board[row][column] == '.']
        self.dfs(board, stack)
