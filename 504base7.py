class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num: return '0'
        else:
            sign = '' if num > 0 else '-'
            num = abs(num)
            result = ''
            while num:
                result = str(num % 7) + result
                num //= 7
            return sign + result
