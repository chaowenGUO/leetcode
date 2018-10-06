# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left + 1 < right:
            middle = left + (right - left) // 2
            if not isBadVersion(middle): left = middle
            else: right = middle
        if isBadVersion(left): return left
        else: return right
