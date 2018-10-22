class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {}
        for index, num in enumerate(nums):
            if num in dictionary: return [index, dictionary.get(num)]
            else: dictionary.setdefault(target - num, index)
