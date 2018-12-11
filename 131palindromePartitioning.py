class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        return [[s[:_]] + rest
               for _ in range(1, len(s) + 1)
               if s[:_] == s[_ - 1::-1]
               for rest in self.partition(s[_:])] or [[]]
