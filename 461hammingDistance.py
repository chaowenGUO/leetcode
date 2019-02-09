class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = 0
        n = x ^ y
        while n:
            n &= n - 1
            result += 1
        return result
