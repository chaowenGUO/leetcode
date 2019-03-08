class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = math.factorial(n)
        result, k = '', (k - 1) % factorial
        *element, = range(1, n + 1)
        while element:
            factorial //= len(element)
            _, k = divmod(k, factorial)
            result += str(element.pop(_))
        return result
