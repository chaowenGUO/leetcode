class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        index = 0
        while index < len(nums) - 2:
            num = nums[index]
            if num > 0: break
            left, right = index + 1, len(nums) - 1
            while left < right:
                numsLeft, numsRight = map(nums.__getitem__, (left, right))
                total = num + numsLeft + numsRight
                if total == 0: result += [num, numsLeft, numsRight],
                if total <= 0:
                    while left < right and nums[left] == numsLeft: left += 1
                if total >= 0:
                    while left < right and nums[right] == numsRight: right -= 1
            while nums[index] == num and index < len(nums) - 2: index += 1
        return result 
