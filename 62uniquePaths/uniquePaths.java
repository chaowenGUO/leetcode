class Solution {
    public int uniquePaths(int m, int n) {
        return Math.toIntExact(LongStream.range(1, m).reduce(1, (result, $) -> result * (n - 1 + $) / $));
    }
}
