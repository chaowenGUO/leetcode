class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = sum(_ & 1 for _ in collections.Counter(s).values())
        return len(s) - odd + bool(odd)
