import functools

class Solution:
    def titleToNumber(self, s: str) -> int:
        return functools.reduce(lambda acc, _: acc * 26 + _, (ord(char) - 64 for char in s))
