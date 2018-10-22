class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[n**2]]
        while matrix[0][0] > 1: matrix = [[*range(matrix[0][0] - len(matrix), matrix[0][0])], *map(list,zip(*reversed(matrix)))]
        return matrix
