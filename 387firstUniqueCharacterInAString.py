class Solution:
    def firstUniqChar(self, s: str) -> int:
        dictionary = collections.Counter(s)
        for index, char in enumerate(s):
            if dictionary.get(char) == 1: return index
        return -1
