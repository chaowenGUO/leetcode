class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import functools, operator
        return functools.reduce(operator.xor, nums)
