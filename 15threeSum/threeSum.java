class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        final var result = new ArrayList<List<Integer>>();
        for (var index = 0; index < nums.length - 2;)
        {
            final var num = nums[index];
            if (num > 0) break;
            var left = index + 1;
            var right = nums.length - 1;
            while (left != right)
            {
                final var numsLeft = nums[left];
                final var numsRight = nums[right];
                final var total = num + numsLeft + numsRight;
                if (total == 0) result.add(List.of(num, numsLeft, numsRight));
                if (total <= 0) while (left != right && numsLeft == nums[left]) ++left;
                if (total >= 0) while (left != right && numsRight == nums[right]) --right;
            }
            while (index < nums.length - 2 && nums[index] == num) ++index;
        }
        return result;
    }
}
