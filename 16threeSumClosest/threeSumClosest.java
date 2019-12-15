class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int result = Arrays.stream(nums).limit(3).sum();
        for (int index = 0; index != nums.length - 2;)
        {
            final int num = nums[index];
            int left = index + 1, right = nums.length - 1;
            while (left != right)
            {
                final int numsLeft = nums[left], numsRight = nums[right];
                final int total = num + numsLeft + numsRight;
                if (total == target) return target;
                if (total <= target) while (left != right && numsLeft == nums[left]) ++left;
                if (total >= target) while (left != right && numsRight == nums[right]) --right;
                if (Math.abs(total - target) < Math.abs(result - target)) result = total;
            }
            while (nums[index] == num && index != nums.length - 2) ++index;
        }
        return result;
    }
}
