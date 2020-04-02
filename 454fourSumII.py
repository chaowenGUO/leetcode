class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        result = collections.Counter(sum(_) for _ in itertools.product(A, B))
        return sum(result[-sum(_)] for _ in itertools.product(C, D))
