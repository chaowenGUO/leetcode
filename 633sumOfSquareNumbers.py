class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        return any(int(math.sqrt(c - _**2))**2 == c - _**2 for _ in range(int(math.sqrt(c)) + 1))
