class Solution:
    def romanToInt(self, s: str) -> int:
        import functools
        dictionary = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        return functools.reduce(lambda result, char: [result[0] - dictionary.get(char) if dictionary.get(char) < dictionary.get(result[1]) else result[0] + dictionary.get(char), char], reversed(s), [0, 'I'])[0]
