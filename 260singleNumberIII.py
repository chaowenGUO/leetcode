class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import functools, operator
        xor = functools.reduce(operator.xor, nums)
        position = xor & -xor
        result = [0] * 2
        for num in nums:
            if num & position: result[0] ^= num
            else: result[1] ^= num
        return result
