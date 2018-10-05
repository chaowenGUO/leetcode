class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        import functools, operator
        return chr(functools.reduce(operator.xor, map(ord, s + t)))
