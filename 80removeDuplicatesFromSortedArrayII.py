class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        for num in nums:
            if index < 2 or num > nums[index - 2]:
                nums[index] = num
                index += 1
        return index
