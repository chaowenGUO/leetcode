class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len({*zip(s, t)}) == len({*s}) == len({*t})
