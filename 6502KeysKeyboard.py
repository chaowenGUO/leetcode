class Solution:
    def minSteps(self, n: int) -> int:
        result = 0
        for _ in range(2, n + 1):
            while not n % _:
                result += _
                n //= _
        return result
