class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import functools
        return functools.reduce(lambda result, num: [result[1], max(result[1], result[0] + num)], nums, [0] * 2)[1]
