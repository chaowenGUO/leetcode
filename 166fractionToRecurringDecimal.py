class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = '-' if numerator * denominator < 0 else ''
        head, remainder = divmod(*map(abs, (numerator, denominator)))
        tail, seen = '', {}
        while remainder:
            if remainder in seen:
                tail = ''.join((tail[:seen[remainder]], '(', tail[seen[remainder]:], ')'))
                break
            seen[remainder] = len(tail)
            digit, remainder = divmod(10 * remainder, abs(denominator))
            tail += str(digit)
        return sign + str(head) + (tail and '.' + tail)
