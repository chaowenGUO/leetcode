class Solution:
    def isNumber(self, s: str) -> bool:
        return bool(re.search('^[+-]?(\.\d+|\d+\.?\d*)(e[+-]?\d+)?$', s.strip()))
