class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ''
        while n:
            n -= 1
            result = chr(n % 26 + 65) + result
            n //= 26
        return result
