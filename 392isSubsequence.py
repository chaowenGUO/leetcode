class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = iter(t)
        return all(item in t for item in s)
