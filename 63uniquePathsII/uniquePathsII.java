class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int[] dp = Arrays.stream(obstacleGrid[0]).map($ -> 1 - $).toArray();
        Arrays.parallelPrefix(dp, Math::multiplyExact);
        Stream.of(obstacleGrid).skip(1).forEach(row -> {
            dp[0] *= 1 - row[0];
            IntStream.range(1, row.length).forEach(column -> dp[column] = IntStream.range(column - 1, column + 1).map($ -> dp[$]).sum() * (1 - row[column]));});
        return dp[dp.length - 1];   
    }
}
