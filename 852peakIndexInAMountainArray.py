import typing
class Solution:
    def peakIndexInMountainArray(self, A: typing.List[int]) -> int:
        left, right = 0, len(A) - 1
        while left + 1 < right:
            middle = left + (right - left) // 2
            if A[middle] < A[middle + 1]: left = middle
            else: right = middle
        return left if A[left] > A[right] else right
