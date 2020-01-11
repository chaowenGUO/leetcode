class Solution {
    public int minPathSum(int[][] grid) {
        int[] dp = grid[0];
        Arrays.parallelPrefix(dp, (a,b) -> a + b);
        Stream.of(grid).skip(1).forEach(row -> {
            dp[0] += row[0];
            IntStream.range(1, row.length).forEach(column -> dp[column] = IntStream.range(column - 1, column + 1).map($ -> dp[$]).min().orElse(0) + row[column]);});
        return dp[dp.length - 1];
    }
}
