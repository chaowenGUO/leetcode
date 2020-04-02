class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        var result = Arrays.stream(nums).limit(3).sum();
        for (var index = 0; index != nums.length - 2;)
        {
            final var num = nums[index];
            var left = index + 1;
            var right = nums.length - 1;
            while (left != right)
            {
                final var numsLeft = nums[left];
                final var numsRight = nums[right];
                final var total = num + numsLeft + numsRight;
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
