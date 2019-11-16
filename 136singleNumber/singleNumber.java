class Solution {
    public int singleNumber(int[] nums) {
        return java.util.Arrays.stream(nums).reduce((a, b) -> a ^ b).orElse(0);
    }
}
