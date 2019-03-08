class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return ''.join(next(zip(*itertools.takewhile(lambda char: len({*char}) == 1, zip(*strs))), ''))
