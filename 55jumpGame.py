class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for index, num in enumerate(nums):
            if index <= reach: reach = max(reach, index + num)
        return reach >= len(nums) - 1
