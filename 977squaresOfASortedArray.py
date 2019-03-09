class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        left, right = 0, len(A) - 1
        result = []
        while left <= right:
            absLeft, absRight = map(abs, (A[left], A[right]))
            if absLeft > absRight:
                result += absLeft**2,
                left += 1
            else:
                result += absRight**2,
                right -= 1
        return result[::-1]
