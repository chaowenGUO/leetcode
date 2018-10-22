class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for row in range(length // 2):
            for column in range(length - length // 2):
                matrix[row][column], matrix[~column][row], matrix[~row][~column], matrix[column][~row] = matrix[~column][row], matrix[~row][~column], matrix[column][~row], matrix[row][column]
