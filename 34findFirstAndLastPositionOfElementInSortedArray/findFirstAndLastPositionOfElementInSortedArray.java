class Solution {
    private static int range(final int[] nums, final int target, final BiPredicate<Integer, Integer> compare)
    {
        int left = 0, right = nums.length;
        while (left != right)
        {
            final int middle = left + (right - left) / 2;
            if (compare.test(nums[middle], target)) left = middle + 1;
            else right = middle;
        }
        return left;
    }
    
    public int[] searchRange(int[] nums, int target) {
        final List<Integer> range = Stream.<BiPredicate<Integer, Integer>>of((a,b) -> a < b, (a,b) -> a <= b).map($ -> this.range(nums, target, $)).collect(Collectors.toList());
        return range.get(0) != range.get(1) ? new int[]{range.get(0), range.get(1) - 1} : IntStream.of(0, 2).map($ -> -1).toArray();
    }
}
