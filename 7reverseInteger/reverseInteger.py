class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        while x:
            if abs(result) > ((1 << 31) - 1) / 10: return 0
            else:
                result = result * 10 + int(math.fmod(x, 10))
                x = int(x / 10)
        return result
