class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ss = (s * 2)[1:-1]
        return s in ss
