class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        return [_[0] for _ in collections.Counter(''.join((A, ' ', B)).split()).items() if _[1] == 1]
