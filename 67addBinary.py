class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        import itertools
        carry = 0
        result = ''
        for _ in itertools.zip_longest(reversed(a), reversed(b), fillvalue = '0'):
            carry += sum(map(int, _))
            result = str(carry & 1) + result
            carry >>= 1
        return '1' + result if carry else result
