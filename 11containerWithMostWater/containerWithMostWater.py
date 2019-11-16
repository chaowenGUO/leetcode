class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1
        while left < right:
            result = max(result, (right - left) * min(map(height.__getitem__, (left, right))))
            if operator.sub(*map(height.__getitem__, (left, right))) < 0: left += 1
            else: right -= 1
        return result
