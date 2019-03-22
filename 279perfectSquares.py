class Solution:
    def numSquares(self, n: int) -> int:
        while not n & 3: n >>= 2
        if n & 7 == 7: return 4
        elif int(math.sqrt(n))**2 == n: return 1
        elif any(int(math.sqrt(n - _**2))**2 == n - _**2 for _ in range(int(math.sqrt(n)) + 1)): return 2
        else: return 3
