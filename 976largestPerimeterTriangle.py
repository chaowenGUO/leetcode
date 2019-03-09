class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A = sorted(A, reverse = True)
        for _ in range(len(A) - 2):
            if A[_] < A[_ + 1] + A[_ + 2]: return A[_] + A[_ + 1] + A[_ + 2]
        return 0
