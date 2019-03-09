class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ''
        carry = 0
        for _ in itertools.zip_longest(reversed(num1), reversed(num2), fillvalue = '0'):
            carry += sum(map(int, _))
            result = str(carry % 10) + result
            carry //= 10
        return '1' + result if carry else result
