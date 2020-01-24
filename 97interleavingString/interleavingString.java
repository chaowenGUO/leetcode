class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        if (s1.codePointCount(0, s1.length()) + s2.codePointCount(0, s2.length()) != s3.codePointCount(0, s3.length())) return false;
        else
        {
            final boolean[] dp = new boolean[s2.codePointCount(0, s2.length()) + 1];
            dp[0] = true;
            IntStream.range(1, dp.length).forEach(column -> dp[column] = dp[column - 1] && s3.codePointAt(column - 1) == s2.codePointAt(column - 1));
            IntStream.range(1, s1.codePointCount(0, s1.length()) + 1).forEach(row -> {
                dp[0] = dp[0] && s3.codePointAt(row - 1) == s1.codePointAt(row - 1);
                IntStream.range(1, dp.length).forEach(column -> dp[column] = dp[column] && s3.codePointAt(row + column - 1) == s1.codePointAt(row - 1) || dp[column - 1] && s3.codePointAt(row + column - 1) == s2.codePointAt(column - 1));});
            return dp[dp.length - 1];
        }
    }
}
