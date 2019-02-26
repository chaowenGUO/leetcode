class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        result = 0
        while X < Y:
            Y = Y + 1 if Y & 1 else Y >> 1
            result += 1
        return result + X - Y
