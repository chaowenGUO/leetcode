# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution:
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left + 1 < right:
            middle = left + (right - left) // 2
            if guess(middle) == 1: left = middle
            else: right = middle
        if guess(left) == 0: return left
        else: return right
