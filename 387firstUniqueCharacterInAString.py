class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary = {}
        for char in s: dictionary[char] = dictionary.get(char, 0) + 1
        for index, char in enumerate(s):
            if dictionary.get(char) == 1: return index
        return -1
