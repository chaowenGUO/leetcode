class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        import itertools
        self.data =[*itertools.accumulate(itertools.chain([0], nums))]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.data[j + 1] - self.data[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
