class Solution {
    public boolean isMatch(String s, String p) {
        boolean[] dp = new boolean[p.codePointCount(0, p.length()) + 1];
        dp[0] = true;
        IntStream.range(2, dp.length).forEach(column -> dp[column] = dp[column - 2] && p.codePointAt(column - 1) == "*".codePointAt(0));
        IntStream.range(1, s.codePointCount(0, s.length()) + 1).forEach(row -> {
            final boolean[] prev = dp.clone();
            dp[0] = false;
            IntStream.range(1, dp.length).forEach(column -> {
                if (s.codePointAt(row - 1) == p.codePointAt(column - 1) || p.codePointAt(column - 1) == ".".codePointAt(0)) dp[column] = prev[column - 1];
                else if (p.codePointAt(column - 1) == "*".codePointAt(0)) dp[column] = dp[column - 2] || prev[column] && (p.codePointAt(column - 2) == s.codePointAt(row - 1) || p.codePointAt(column - 2) == ".".codePointAt(0));
                else dp[column] = false;});});
        return dp[dp.length - 1];
    }
}
