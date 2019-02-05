import typing
class Solution:
    def searchMatrix(self, matrix: typing.List[typing.List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        else:
            column = len(matrix[0])
            left, right = 0, len(matrix) * column - 1
            while left + 1 < right:
                middle = left + (right - left) // 2
                if matrix[middle // column][middle % column] < target: left = middle
                else: right = middle
            return True if matrix[left // column][left % column] == target or matrix[right // column][right % column] == target else False
