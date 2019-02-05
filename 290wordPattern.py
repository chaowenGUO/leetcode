class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str = str.split()
        return len({*str}) == len({*pattern}) == len({*zip(str, pattern)}) and len(str) == len(pattern)
