class Solution:
    def judgeCircle(self, moves: str) -> bool:
        import collections
        dictionary = collections.Counter(moves)
        return dictionary.get('L') == dictionary.get('R') and dictionary.get('U') == dictionary.get('D')
