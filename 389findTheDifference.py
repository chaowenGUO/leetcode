import functools

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(functools.reduce(operator.xor, map(ord, s + t)))
