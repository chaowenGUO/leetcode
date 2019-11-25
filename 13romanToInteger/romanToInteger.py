import functools

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        return functools.reduce(lambda result, _: [result[0] - roman.get(_) if operator.lt(*map(roman.get, (_, result[1]))) else result[0] + roman.get(_), _], reversed(s), [0, 'I'])[0]
