class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        import functools
        return functools.reduce(lambda acc, elem: acc * 26 + elem, (ord(char) - 64 for char in s))
