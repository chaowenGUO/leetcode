class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        else:
            result = [''] * numRows
            row, direction = 0, 1
            for char in s:
                result[row] += char
                if row == 0: direction = 1
                elif row == numRows - 1: direction = -1
                row += direction
            return ''.join(result)
