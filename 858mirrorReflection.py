class Solution:
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        import math
        gcd = math.gcd(p, q)
        p = p // gcd
        q = q // gcd
        return 1 - (p & 1) + (q & 1)
