class Solution {
    public int findNumbers(int[] nums) {
        return Math.toIntExact(Arrays.stream(nums).map(num -> 1 - Integer.toString(num).length() & 1).filter($ -> $ == 1).count());
    }
}
