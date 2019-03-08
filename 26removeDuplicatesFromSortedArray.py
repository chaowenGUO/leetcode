class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1 if nums else 0
        for num in nums:
            if num > nums[index - 1]:
                nums[index] = num
                index += 1
        return index
