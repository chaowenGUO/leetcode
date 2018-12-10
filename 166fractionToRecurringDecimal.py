class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = '-' if numerator * denominator < 0 else ''
        head, remainder = divmod(abs(numerator), abs(denominator))
        tail, seen = '', {}
        while remainder:
            if remainder in seen:
                tail = tail[:seen[remainder]] + '(' + tail[seen[remainder]:] + ')'
                break
            seen[remainder] = len(tail)
            digit, remainder = divmod(remainder * 10, abs(denominator))
            tail += str(digit)
        return sign + str(head) + (tail and '.' + tail)
