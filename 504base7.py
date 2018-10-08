class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num: return '0'
        result = ''
        sign = '' if num > 0 else '-'
        num = abs(num)
        while num:
            result = str(num % 7) + result
            num //= 7
        return sign + result
