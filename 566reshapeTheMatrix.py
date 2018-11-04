class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        import itertools
        if len(nums) * len(nums[0]) != r * c: return nums
        else:
            data = itertools.chain(*nums)
            return [[*itertools.islice(data, c)] for _ in range(r)]
