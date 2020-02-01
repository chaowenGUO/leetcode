class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return [1 - len(str(num)) & 1 for num in nums].count(1)
