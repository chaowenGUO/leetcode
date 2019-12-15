class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        final ArrayList<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        for (int index = 0; index < nums.length - 2;)
        {
            final int num = nums[index];
            if (num > 0) break;
            int left = index + 1, right = nums.length - 1;
            while (left != right)
            {
                final int numsLeft = nums[left], numsRight = nums[right];
                final int total = num + numsLeft + numsRight;
                if (total == 0) result.add(Arrays.asList(num, numsLeft, numsRight));
                if (total <= 0) while (left != right && nums[left] == numsLeft) ++left;
                if (total >= 0) while (left != right && nums[right] == numsRight)  --right;
            }
            while (nums[index] == num && index < nums.length - 2) ++index;
        }
        return result;
    }
}
