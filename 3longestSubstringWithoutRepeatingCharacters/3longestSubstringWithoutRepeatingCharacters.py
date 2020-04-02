class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = left = right = 0
        characters = set()
        while right < len(s):
            if s[right] not in characters:
                characters.add(s[right])
                right += 1
                result = max(result, len(characters))
            else:
                characters.discard(s[left])
                left += 1
        return result
