class Solution:
    def __getitem__(self, index):
        return self.after >= index + 1 and self.nums1[index] - self.nums2[self.after - index - 1]
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1
        self.after = (len(nums1) + len(nums2) - 1) // 2
        self.nums1 = nums1
        self.nums2 = nums2
        left = bisect.bisect_left(self, 0, 0, len(nums1))
        result = sorted((*itertools.islice(nums1, left, left + 2), *itertools.islice(nums2, self.after - left, self.after - left + 2)))
        return (result[0] + result[1 - (len(nums1) + len(nums2)) & 1]) / 2
