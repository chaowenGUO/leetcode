class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1]]
        for _ in range(numRows - 1): result += [sum(_) for _ in zip([0] + result[-1], result[-1] + [0])],
        return result[:numRows]
