class Solution {
    public int minDistance(String word1, String word2) {
        int[] dp = IntStream.range(0, word2.codePointCount(0, word2.length()) + 1).toArray();
        IntStream.range(1, word1.codePointCount(0, word1.length()) + 1).forEach(row -> {
            int[] prev = dp.clone();
            dp[0] = row;
            IntStream.range(1, dp.length).forEach(column -> dp[column] = (int)DoubleStream.of(dp[column - 1] + 1, prev[column] + 1, prev[column - 1] + 1, word1.codePointAt(row - 1) == word2.codePointAt(column - 1) ? prev[column - 1] : Double.POSITIVE_INFINITY).min().orElse(0));});
        return dp[dp.length - 1];
    }
}
