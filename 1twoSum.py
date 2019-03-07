class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for index, num in enumerate(nums):
            if num in dictionary: return [index, dictionary.get(num)]
            else: dictionary.setdefault(target - num, index)
