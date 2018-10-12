class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split()
        return len({*zip(pattern, str)}) == len({*pattern}) == len({*str}) and len(str) == len(pattern)
