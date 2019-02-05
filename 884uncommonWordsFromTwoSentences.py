import typing
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> typing.List[str]:
        import collections
        return [_[0] for _ in collections.Counter((A + ' ' + B).split()).items() if _[1] == 1]
