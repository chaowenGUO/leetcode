class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = left = 0
        dictionary = {}
        for index, char in enumerate(s):
            if char in dictionary and left <= dictionary.get(char): left = dictionary.get(char) + 1
            else: result = max(result, index - left + 1)
            dictionary[char] = index
        return result
