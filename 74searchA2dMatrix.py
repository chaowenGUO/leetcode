class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        column = len(matrix[0])
        left, right = 0, len(matrix) * column - 1
        while left + 1 < right:
            middle = left + (right - left) // 2
            if matrix[middle // column][middle % column] < target: left = middle
            else: right = middle
        if matrix[left // column][left % column] == target or matrix[right // column][right % column] == target: return True
        else: return False
