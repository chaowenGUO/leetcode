class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()        
        dictionary = {key:{*group} for key, group in itertools.groupby(sorted(filter(lambda _: operator.lt(*_), itertools.product(range(len(nums)), repeat = 2)), key = lambda _: sum(map(nums.__getitem__, _))), lambda _: sum(map(nums.__getitem__, _)))}
        result = set()
        for left in range(2, len(nums) - 1):
            for right in range(left + 1, len(nums)):
                if (complement := target - sum(map(nums.__getitem__, (left, right)))) in dictionary: result.update(tuple(map(nums.__getitem__, (*_, left, right)))  for _ in dictionary.get(complement) if _[1] < left)
        return [[*_] for _ in result]
