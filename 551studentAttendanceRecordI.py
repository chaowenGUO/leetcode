class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s.count('A') <= 1 and 'L' * 3 not in s
