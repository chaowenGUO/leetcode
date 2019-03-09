class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        gcd = math.gcd(p, q)
        p //= gcd
        q //= gcd
        return 1 - (p & 1) + (q & 1)
