class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for num in sorted(nums): result += [_ + [num] for _ in result if _ + [num] not in result]
        return result
