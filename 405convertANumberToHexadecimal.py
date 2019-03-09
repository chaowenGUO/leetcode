class Solution:
    def toHex(self, num: int) -> str:
        if not num: return '0'
        else:
            result = ''
            for _ in range(8):
                result = (string.digits + 'abcdef')[num & 15] + result
                num >>= 4
            return result.lstrip('0')
