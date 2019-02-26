class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums) * len(nums[0]) != r * c: return nums
        else:
            data = itertools.chain(*nums)
            return [[*itertools.islice(data, c)] for _ in range(r)]
