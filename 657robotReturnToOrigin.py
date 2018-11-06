class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        import collections
        dictionary = collections.Counter(moves)
        return dictionary.get('U') == dictionary.get('D') and dictionary.get('L') == dictionary.get('R')
