class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority0, majority1, count0, count1 = 0, 1, 0, 0
        for num in nums:
            if majority0 == num: count0 += 1
            elif majority1 == num: count1 += 1
            elif count0 == 0: majority0, count0 = num, 1
            elif count1 == 0: majority1, count1 = num, 1
            else:
                count0 -= 1
                count1 -= 1
        return [majority for majority in (majority0, majority1) if nums.count(majority) > len(nums) // 3]
