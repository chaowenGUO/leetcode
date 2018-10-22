class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        return bool(re.search('^[+-]?(\.\d+|\d+\.?\d*)(e[+-]?\d+)?$', s.strip()))
