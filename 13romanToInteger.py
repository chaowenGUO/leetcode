class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        result, p = 0, 'I'
        for char in reversed(s): result, p = result - dictionary.get(char) if dictionary.get(char) < dictionary.get(p) else result + dictionary.get(char), char
        return result
