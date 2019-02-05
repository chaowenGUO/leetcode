class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num // 2 + 1
        while left + 1 < right:
            middle = left + (right - left) // 2
            if middle**2 < num: left = middle
            else: right = middle
        return True if left**2 == num or right**2 == num else False
