class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A') <= 1 and 'L' * 3 not in s
