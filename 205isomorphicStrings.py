class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len({*s}) == len({*t}) == len({*zip(s, t)})
