import functools

class Solution:
    def toHex(self, num: int) -> str:
        return functools.reduce(lambda result, _: [(string.digits + 'abcdef')[result[1] & 15] + result[0], result[1] >> 4], range(8), ['', num])[0].lstrip('0') if num else '0'
