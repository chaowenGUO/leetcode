class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        carry = 0
        for _ in itertools.zip_longest(reversed(a), reversed(b), fillvalue = '0'):
            carry += sum(map(int, _))
            result = str(carry & 1) + result
            carry >>= 1
        return '1' + result if carry else result
