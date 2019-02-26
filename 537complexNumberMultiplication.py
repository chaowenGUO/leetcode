class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a0, a1 = map(int, a[:-1].split('+'))
        b0, b1 = map(int, b[:-1].split('+'))
        return ''.join((str(a0 * b0 - a1 * b1), '+', str(a0 * b1 + a1 * b0), 'i'))
