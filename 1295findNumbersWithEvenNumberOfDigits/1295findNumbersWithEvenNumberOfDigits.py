class Solution:
    @staticmethod
    def even(num):
        result = 0
        while num:
            num //= 10
            result += 1
        return 1 - result & 1
    
    def findNumbers(self, nums: List[int]) -> int:
        return sum(map(self.even, nums))
