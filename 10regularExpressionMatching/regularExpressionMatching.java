class Solution {
    public boolean isMatch(String s, String p) {
        boolean[] dp = new boolean[p.codePointCount(0, p.length()) + 1];
        dp[0] = true;
        for (int column = 2; column < dp.length; ++column)
            if (p.codePointAt(column - 1) == "*".codePointAt(0)) dp[column] = dp[column - 2];
        boolean[] prev = dp.clone();
        for (int row = 1; row != s.codePointCount(0, s.length()) + 1; ++row)
        {
            dp[0] = false;
            for (int column = 1; column != dp.length; ++column)
            {
                if (s.codePointAt(row - 1) == p.codePointAt(column - 1) || p.codePointAt(column - 1) == ".".codePointAt(0)) dp[column] = prev[column - 1];
                else if (p.codePointAt(column - 1) == "*".codePointAt(0))
                {
                    if (p.codePointAt(column - 2) == s.codePointAt(row - 1) || p.codePointAt(column - 2) == ".".codePointAt(0)) dp[column] = dp[column - 2] || prev[column];
                    else dp[column] = dp[column - 2];
                }
                else dp[column] = false;
            }
            boolean[] tmp = prev;
            prev = dp;
            dp = tmp;
        }
        return prev[prev.length - 1];
    }
}
