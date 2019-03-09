class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        increase = decrease = True
        for _ in range(len(A) - 1):
            if A[_] > A[_ + 1]: increase = False
            elif A[_] < A[_ + 1]: decrease = False
        return increase or decrease
