class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1, *itertools.repeat(0, rowIndex)]
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1): result[j] += result[j - 1]
        return result
