class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        return sorted(range(1, N + 1), key = lambda _: bin(_)[:1:-1])
