class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = count = 0
        for num in nums:
            if majority == num: count += 1
            elif count == 0: majority, count = num, 1
            else: count -= 1
        return majority
