class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        import itertools
        return sum(1 for _ in itertools.takewhile(lambda char: char != ' ', reversed(s.strip())))
