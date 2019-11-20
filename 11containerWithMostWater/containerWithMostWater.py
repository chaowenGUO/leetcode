class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        result = 0
        while left < right:
            result = max(result, (right - left) * min(map(height.__getitem__, (left, right))))
            (left := left + 1) if operator.sub(*map(height.__getitem__, (left, right))) < 0 else (right := right - 1)
        return result
