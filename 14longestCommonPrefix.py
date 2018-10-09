class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ''
        for char in zip(*strs):
            if len({*char}) == 1: result += char[0]
            else: break
        return result
