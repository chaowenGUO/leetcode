class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        return any(collections.Counter(str(N)) == collections.Counter(str(1 << _)) for _ in range(31))
