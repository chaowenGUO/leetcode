class Solution:
    def countSegments(self, s: str) -> int:
        return sum(s[_] != ' ' and (_ == 0 or s[_ - 1] == ' ') for _ in range(len(s)))
