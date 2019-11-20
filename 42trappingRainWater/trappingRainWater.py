class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        result = level = 0
        while left < right:
            low = min(height[left], height[right])
            (left := left + 1) if height[left] < height[right] else (right := right - 1)
            level = max(level, low)
            result += level - low
        return result
