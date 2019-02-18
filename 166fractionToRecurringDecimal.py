class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = '-' if numerator * denominator < 0 else ''
        head, remainder = divmod(abs(numerator), abs(denominator))
        tail, seen = '', {}
        while remainder:
            if remainder in seen:
                tail = ''.join((tail[:seen[remainder]], '(', tail[seen[remainder]:], ')'))
                break
            seen[remainder] = len(tail)
            digit, remainder = divmod(remainder * 10, abs(denominator))
            tail += str(digit)
        return ''.join((sign, str(head), (tail and '.' + tail)))
