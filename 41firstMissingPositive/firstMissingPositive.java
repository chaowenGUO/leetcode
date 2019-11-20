class Solution {
    public int firstMissingPositive(int[] nums) {
        java.util.stream.IntStream.range(0, nums.length).forEach(index -> {
            while (0 <= nums[index] - 1 && nums[index] - 1 < nums.length && nums[nums[index] - 1] != nums[index])
            {
                int temp = nums[nums[index] - 1];
                nums[nums[index] - 1] = nums[index];
                nums[index] = temp;
            }});
        for (int index = 0; index != nums.length ; ++index)
            if (nums[index] != index + 1) return index + 1;
        return nums.length + 1;        
    }
}
