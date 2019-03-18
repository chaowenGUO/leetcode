cclass Solution:
    def reverse(self, x: int) -> int:
        sign = (x > 0) - (x < 0)
        result = 0
        x = abs(x)
        while x:
            result = result * 10 + x % 10
            x //= 10
        result = sign * result
        return result if -1 << 31 <= result <= (1 << 31) - 1 else 0
