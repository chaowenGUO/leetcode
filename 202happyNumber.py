class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1 and n != 4:
            result = 0
            while n:
                result += (n % 10)**2
                n //= 10
            n = result
        return n == 1
