import functools

class Solution:
    def reverseBits(self, n: int) -> int:
        return functools.reduce(lambda result, _: [result[0] << 1 | result[1] & 1, result[1] >> 1], range(32), [0, n])[0]
