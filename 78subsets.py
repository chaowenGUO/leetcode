class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import functools
        return functools.reduce(lambda result, num: result + [_ + [num] for _ in result], nums, [[]])
