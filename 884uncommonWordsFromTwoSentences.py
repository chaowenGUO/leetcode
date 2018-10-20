class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        import collections
        return [word[0] for word in collections.Counter((A + ' ' + B).split()).items() if word[1] == 1]
