class NumArray:
    import typing
    def __init__(self, nums: typing.List[int]):
        import itertools
        *self.data, = itertools.accumulate(itertools.chain([0], nums)) 

    def sumRange(self, i: int, j: int) -> int:
        return self.data[j + 1] - self.data[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
