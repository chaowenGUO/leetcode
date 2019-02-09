class Solution:
    def frequencySort(self, s: str) -> str:
        import collections, operator
        return ''.join(operator.mul(*_) for _ in collections.Counter(s).most_common())
