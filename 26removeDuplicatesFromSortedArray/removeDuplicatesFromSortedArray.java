class Solution {
    public int removeDuplicates(int[] nums) {
        int index = nums.length != 0 ? 1 : 0;
        for (final var num: nums)
            if (num > nums[index - 1])
            {
                nums[index] = num;
                ++index;
            }
        return index;
    }
}
