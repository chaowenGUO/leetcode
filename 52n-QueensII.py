class Solution:
    def count(self, column, left, right):
        count = 0
        available = self.nbit & ~(column | left | right)
        while available:
            position = available & - available
            available ^= position
            count += self.count(column | position, (left | position) << 1, (right | position) >> 1)
        count += column == self.nbit
        return count
        
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.nbit = (1 << n) - 1
        return self.count(0, 0, 0)
