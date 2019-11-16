class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = sum(itertools.islice(nums, 3))
        index = 0
        while index != len(nums) - 2:
            num = nums[index]
            left, right = index + 1, len(nums) - 1
            while left < right:
                numsLeft, numsRight = map(nums.__getitem__, (left, right))
                total = num + numsLeft + numsRight
                if total == target: return target 
                if total <= target:
                    while left < right and nums[left] == numsLeft: left += 1
                if total >= target:
                    while left < right and nums[right] == numsRight: right -= 1                             
                if abs(target-total) < abs(result - target): result = total           
            while index != len(nums) - 2 and nums[index] == num: index += 1
        return result
