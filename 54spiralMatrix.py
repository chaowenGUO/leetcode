class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        return matrix and matrix.pop(0) + self.spiralOrder([*map(list,zip(*matrix))][::-1])
