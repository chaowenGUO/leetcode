class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        import itertools
        carry = 0
        result = ''
        for _ in itertools.zip_longest(reversed(num1), reversed(num2), fillvalue = '0'):
            carry += sum(map(int, _))
            result = str(carry % 10) + result
            carry //= 10
        return '1' + result if carry else result
