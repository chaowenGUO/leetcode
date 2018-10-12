class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for num in nums: result = [permutation[index:] + [num] + permutation[:index] for permutation in result for index in range((permutation + [num]).index(num) + 1)]
        return result
