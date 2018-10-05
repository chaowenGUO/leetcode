class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = 0
        for num in nums:
            if num:
                nums[index] = num
                index += 1
        nums[index:] = [0] *(len(nums) - index)
