import typing
class Solution:
    def longestCommonPrefix(self, strs: typing.List[str]) -> str:
        import itertools
        return ''.join(next(zip(*itertools.takewhile(lambda char: len({*char}) == 1, zip(*strs))), ''))
