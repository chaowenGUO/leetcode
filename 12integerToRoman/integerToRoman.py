import enum

@enum.unique
class Roman(enum.Enum):
    M = 1000
    CM = 900
    D = 500
    CD = 400
    C = 100
    XC = 90
    L = 50
    XL = 40
    X = 10
    IX = 9
    V = 5
    IV = 4
    I = 1

class Solution:
    def intToRoman(self, num: int) -> str:
        result = []
        for _ in Roman:
            result += itertools.repeat(_.name, num // _.value)
            num %= _.value
        return ''.join(result)
