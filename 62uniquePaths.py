import functools

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return functools.reduce(lambda result, _: result * (n - 1 + _) // _, range(1, m), 1)
