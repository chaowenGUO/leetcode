class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        factorial = math.factorial(n)
        elements = [*range(1, n + 1)]
        k, result = (k - 1) % factorial, ''
        while elements:
            factorial //= len(elements)
            i, k = divmod(k, factorial)
            result += str(elements.pop(i))
        return result
