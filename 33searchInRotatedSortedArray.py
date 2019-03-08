class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        else:
            left, right = 0, len(nums) - 1
            while left + 1 < right:
                middle = left + (right - left) // 2
                if nums[left] < nums[middle]:
                    if nums[left] <= target < nums[middle]: right = middle
                    else: left = middle
                else:
                    if nums[middle] < target <= nums[right]: left = middle
                    else: right = middle
            if nums[left] == target: return left
            elif nums[right] == target: return right
            else: return -1
