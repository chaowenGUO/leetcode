class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for index in range(len(nums)):
            while 0 <= nums[index] - 1 < len(nums) and nums[nums[index] - 1] != nums[index]: nums[nums[index] - 1], nums[index] = nums[index], nums[nums[index] - 1]
        for index in range(len(nums)):
            if nums[index] != index + 1: return index + 1
        return len(nums) + 1
