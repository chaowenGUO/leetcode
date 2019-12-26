class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return operator.eq(*map(collections.Counter, (s, t)))
