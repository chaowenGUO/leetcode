import functools

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        return [*functools.reduce(collections.Counter.__and__, map(collections.Counter, A)).elements()]
