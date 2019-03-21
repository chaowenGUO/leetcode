class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if nums[left] < nums[right]: return nums[left]
        else:
            while left + 1 < right:
                middle = left + (right - left) // 2
                if nums[left] < nums[middle]: left = middle
                else: right = middle
            return min(nums[left], nums[right])
