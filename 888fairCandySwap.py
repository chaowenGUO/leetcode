class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff = (sum(A) - sum(B)) // 2
        A = {*A}
        for _ in {*B}:
            if diff + _ in A: return [_ + diff, _]
