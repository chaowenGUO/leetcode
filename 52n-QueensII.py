class Solution:
    def count(self, column: int, left: int, right: int) -> int:
        count = 0
        available = self.nbit & ~(column | left | right)
        while available:
            position = available & -available
            available ^= position
            count += self.count(position | column, (position | left) << 1, (position | right) >> 1)
        count += self.nbit == column
        return count
    
    def totalNQueens(self, n: int) -> int:
        self.nbit = (1 << n) - 1
        return self.count(0, 0, 0)
