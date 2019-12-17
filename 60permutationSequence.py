class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = math.factorial(n)
        result, k = [], k - 1
        *elements, = range(1, n + 1)
        while elements:
            factorial //= len(elements)
            _, k = divmod(k, factorial)
            result += elements.pop(_),
        return ''.join(map(str, result))
