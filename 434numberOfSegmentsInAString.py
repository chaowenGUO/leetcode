class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum(s[_] != ' ' and (_ == 0 or s[_ - 1] == ' ') for _ in range(len(s)))
