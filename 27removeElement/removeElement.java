class Solution {
    public int removeElement(int[] nums, int val) {
        int index = 0;
        for (final int num: nums)
            if (num != val)
            {
                nums[index] = num;
                ++index;
            }
        return index;
    }
}
