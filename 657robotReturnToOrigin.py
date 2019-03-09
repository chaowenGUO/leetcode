class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dictionary = collections.Counter(moves)
        return dictionary.get('U') == dictionary.get('D') and dictionary.get('L') == dictionary.get('R')
