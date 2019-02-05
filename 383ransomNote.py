class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        import collections
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
