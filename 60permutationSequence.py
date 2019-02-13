class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        factorial = math.factorial(n)
        result, k = '', (k - 1) % factorial
        *elements, = range(1, n + 1)
        while elements:
            factorial //= len(elements)
            _, k = divmod(k, factorial)
            result += str(elements.pop(_))
        return result
