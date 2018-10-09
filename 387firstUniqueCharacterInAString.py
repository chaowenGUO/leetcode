class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        dictionary = collections.Counter(s)
        for index, char in enumerate(s):
            if dictionary.get(char) == 1: return index
        return -1
