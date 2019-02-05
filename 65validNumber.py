class Solution:
    def isNumber(self, s: str) -> bool:
        import re
        return bool(re.search('^[+-]?(\.\d+|\d+\.?\d*)(e[+-]?\d+)?$', s.strip()))
