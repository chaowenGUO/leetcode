class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        for _ in range(len(s) - 1, -1, -1): result += s[_]
        return result
