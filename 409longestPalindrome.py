class Solution:
    def longestPalindrome(self, s: str) -> int:
        import collections
        odd = sum(_ & 1 for _ in collections.Counter(s).values())
        return len(s) - odd + bool(odd)
