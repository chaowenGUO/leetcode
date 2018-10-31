class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        result = [''] * numRows
        row, direction = 0, 1
        for char in s:
            result[row] += char 
            if row == 0: direction = 1
            elif row == numRows - 1: direction = -1
            row += direction
        return ''.join(result)
