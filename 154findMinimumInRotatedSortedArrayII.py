class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            if nums[left] < nums[right]: return nums[left]
            else:
                middle = left + (right - left) // 2
                if nums[left] < nums[middle]: left = middle
                elif nums[left] == nums[middle]: left += 1
                else: right = middle
        return min(nums[left], nums[right])
