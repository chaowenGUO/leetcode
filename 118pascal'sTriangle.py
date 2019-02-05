import typing
class Solution:
    def generate(self, numRows: int) -> typing.List[typing.List[int]]:
        import functools
        return functools.reduce(lambda result, _: result + [[sum(_) for _ in zip([0] + result[-1], result[-1] + [0])]], range(numRows - 1), [[1]])[:numRows]
