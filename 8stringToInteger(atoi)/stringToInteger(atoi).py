class Solution:
    def myAtoi(self, str: str) -> int:
        result = re.search('^[+-]?\d+', str.strip())
        result = int(result[0] if result else 0)
        return statistics.median((-1 << 31, (1 << 31) - 1, result))
