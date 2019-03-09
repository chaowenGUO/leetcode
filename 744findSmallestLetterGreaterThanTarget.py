class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        while left + 1 < right:
            middle = left + (right - left) // 2
            if letters[middle] <= target: left = middle
            else: right = middle
        if letters[left] > target: return letters[left]
        elif letters[right] > target: return letters[right]
        else: return letters[0]
