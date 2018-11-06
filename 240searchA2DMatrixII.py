class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        else:
            j = -1
            for row in matrix:
                while j + len(row) and row[j] > target: j -= 1
                if row[j] == target: return True
            return False
