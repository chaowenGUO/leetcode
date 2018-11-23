class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, remain = 0, {*nums}
        while remain:
            left = right = remain.pop()
            while left - 1 in remain:
                remain.remove(left - 1)
                left -= 1
            while right + 1 in remain:
                remain.remove(right + 1)
                right += 1
            result = max(result, right - left + 1)
        return result
