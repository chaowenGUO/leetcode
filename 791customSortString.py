class Solution:
    def customSortString(self, S: str, T: str) -> str:
        return ''.join(sorted(T, key = lambda _: S.find(_)))
