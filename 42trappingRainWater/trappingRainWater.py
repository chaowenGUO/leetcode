class Solution:
    def trap(self, height: List[int]) -> int:
        result = level = 0
        left, right = 0, len(height) - 1
        while left < right:
            low = min(map(height.__getitem__, (left, right)))
            (left:= left + 1) if operator.lt(*map(height.__getitem__, (left, right))) else (right := right - 1)
            level = max(level, low)
            result += level - low
        return result
