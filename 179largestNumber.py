class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        return str(int(''.join(sorted(map(str, nums), key = lambda _: _ * 9, reverse = True))
