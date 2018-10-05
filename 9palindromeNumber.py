class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or x % 10 == 0 and x != 0: return False
        else:
            result = 0
            while result < x:
                result = result * 10 + x % 10
                x //= 10
            return result == x or result // 10 == x
