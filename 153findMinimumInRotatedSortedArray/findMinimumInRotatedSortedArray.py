class Solution:
    def __getitem__(self, index):
        return -self.__nums[index]
    
    def findMin(self, nums: List[int]) -> int:
        self.__nums = nums
        return nums[bisect.bisect_left(self, -nums[-1], 0, len(nums))]
