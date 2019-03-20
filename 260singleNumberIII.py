import functools

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = functools.reduce(operator.xor, nums)
        position = xor & -xor
        result = [0] * 2
        for num in nums:
            if position & num: result[0] ^= num
            else: result[1] ^= num
        return result
