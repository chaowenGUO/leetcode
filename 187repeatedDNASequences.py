class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        return [_[0] for _ in collections.Counter(s[_:_ + 10] for _ in range(len(s) - 9)).items() if _[1] > 1]
