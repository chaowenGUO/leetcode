class Solution:
    def __getitem__(self, index):
        return index**2
    
    def mySqrt(self, x: int) -> int:
        left = bisect.bisect_left(self, x, 0, x // 2 + 1)
        return left if left**2 == x else left - 1
