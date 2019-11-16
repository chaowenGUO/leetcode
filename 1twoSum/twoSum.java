class Solution {
    public int[] twoSum(int[] nums, int target) {
        final HashMap<Integer, Integer> dictionary = new HashMap<>();
        for (int index = 0;; ++index)
        {
            final int num = nums[index];
            if (dictionary.containsKey(num)) return new int[]{index, dictionary.get(num)};
            else dictionary.putIfAbsent(target - num, index);
        }
    }
}
