class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dictionary = collections.Counter(nums)
        return max((dictionary.get(_) + dictionary.get(_ + 1) for _ in dictionary if _ + 1 in dictionary), default = 0)
