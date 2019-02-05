# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left + 1 < right:
            middle = left + (right - left) // 2
            if not isBadVersion(middle): left = middle
            else: right = middle
        return left if isBadVersion(left) else right
