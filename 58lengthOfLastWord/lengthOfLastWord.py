import functools

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return sum(1 for _ in itertools.takewhile(functools.partial(operator.ne, ' '), reversed(s.strip())))
