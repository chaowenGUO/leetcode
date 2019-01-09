class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1] + [0] * rowIndex
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1): result[j] += result[j - 1]
        return result
