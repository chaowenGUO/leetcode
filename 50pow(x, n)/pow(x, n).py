class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        sign = math.copysign(1, n)
        while n:
            if n & 1: result *= x
            x *= x
            n = int(n / 2)
        return result if sign == 1 else 1 / result
