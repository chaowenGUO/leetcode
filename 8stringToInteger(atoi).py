class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re
        try:
            result = int(re.search('^[+-]?\d+', str.strip()).group())
            return max(-(1 << 31), min((1 << 31) - 1, result))
        except: return 0
