class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        index = 1
        while index <= num: index <<= 1
        return num ^ (index - 1)
