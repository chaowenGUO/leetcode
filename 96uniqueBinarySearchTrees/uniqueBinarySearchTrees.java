class Solution {
    public int numTrees(int n) {
        return Math.toIntExact(LongStream.range(0, n).reduce(1, (catalan, $) -> catalan * 2 * (2 * $ + 1) / ($ + 2)));
    }
}
