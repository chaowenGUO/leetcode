class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        left, right = 0, len(A) - 1
        while left < right:
            if A[left] & 1 == 0: left += 1
            elif A[right] & 1 == 1: right -= 1
            else: A[left], A[right] = A[right], A[left]
        return A
