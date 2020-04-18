class Solution {
    public int removeElement(int[] nums, int val) {
        var index = 0;
        for (final var num: nums)
            if (num != val)
            {
                nums[index] = num;
                ++index;
            }
        return index;
    }
}
