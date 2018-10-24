class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        import collections
        return [_[0] for _ in collections.Counter((A + ' ' + B).split()).items() if _[1] == 1]
