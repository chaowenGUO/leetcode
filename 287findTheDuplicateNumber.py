class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = fast = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                slow = 0
                while fast != slow:
                    fast = nums[fast]
                    slow = nums[slow]
                return slow
