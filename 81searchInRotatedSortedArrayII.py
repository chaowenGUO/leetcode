class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums: return False
        else:
            left, right = 0, len(nums) - 1
            while left + 1 < right:
                middle = left + (right - left) // 2
                if nums[left] < nums[middle]:
                    if nums[left] <= target < nums[middle]: right = middle
                    else: left = middle
                elif nums[left] == nums[middle]: left += 1
                else:
                    if nums[middle] < target <= nums[right]: left = middle
                    else: right = middle
            return True if nums[left] == target or nums[right] == target else False
