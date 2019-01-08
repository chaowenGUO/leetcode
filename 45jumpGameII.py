class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = reach = maxReach = 0
        for index, num in enumerate(nums):
            if index > reach:
                reach = maxReach
                result += 1
            maxReach = max(maxReach, index + num)
        return result
