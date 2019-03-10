import functools

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return functools.reduce(lambda result, _: [*result, [*map(operator.add, itertools.chain([0], result[-1]), itertools.chain(result[-1], [0]))]], range(numRows - 1), [[1]])[:numRows]
