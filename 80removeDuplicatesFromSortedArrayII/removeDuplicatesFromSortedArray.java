class Solution {
    public int removeDuplicates(int[] nums) {
        int index = 0;
        for (final int num: nums)
        {
            if (index < 2 || num > nums[index - 2])
            {
                nums[index] = num;
                ++index;
            }
        }
        return index;
    }
}
