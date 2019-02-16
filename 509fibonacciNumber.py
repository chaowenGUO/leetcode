class Solution:
    def fib(self, N: int) -> int:
        import functools
        return functools.reduce(lambda result, _: [result[1], sum(result)], range(N), [0, 1])[0]
