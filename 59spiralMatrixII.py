class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[n**2]]
        while result[0][0] > 1: result = [[*range(result[0][0] - len(result), result[0][0])], *map(list, zip(*reversed(result)))]
        return result
