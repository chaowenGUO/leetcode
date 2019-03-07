import functools

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return functools.reduce(lambda result, _: result + [[sum(_) for _ in zip(itertools.chain([0], result[-1]), itertools.chain(result[-1], [0]))]], range(numRows - 1), [[1]])[:numRows]
