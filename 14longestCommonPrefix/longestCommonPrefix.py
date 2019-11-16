class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return ''.join(next(zip(*itertools.takewhile(lambda _: len({*_}) == 1, zip(*strs))), ''))
