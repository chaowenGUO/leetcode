class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [_[0] for _ in collections.Counter(nums).most_common(k)]
