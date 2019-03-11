import functools

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return functools.reduce(lambda result, _: [[_] + combination for combination in result for _ in range(1, combination[0] if combination else n + 1)], range(k), [[]])
