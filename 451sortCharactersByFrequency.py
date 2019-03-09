class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(operator.mul(*_) for _ in collections.Counter(s).most_common())
