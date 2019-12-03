class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        dictionary = collections.defaultdict(list)
        for left in range(len(nums) - 1):
            for right in range(left + 1, len(nums)): dictionary[sum(map(nums.__getitem__, (left, right)))] += [left, right],
        result = set()
        for left in range(2, len(nums) - 1):
            for right in range(left + 1, len(nums)):
                if (complement := target - sum(map(nums.__getitem__, (left, right)))) in dictionary: result.update(tuple(map(nums.__getitem__, (*_, left, right))) for _ in dictionary.get(complement) if _[1] < left)
        return [[*_] for _ in result]
