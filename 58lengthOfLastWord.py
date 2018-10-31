class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for _ in reversed(s.strip()):
            if _ != ' ': result += 1
            else: break
        return result
