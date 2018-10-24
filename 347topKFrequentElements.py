class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections
        return [_[0] for _ in collections.Counter(nums).most_common(k)]
