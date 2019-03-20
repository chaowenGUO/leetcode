class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        else:
            for row in matrix:
                for column in reversed(row):
                    if column <= target: break
                if column == target: return True
            return False
