class Solution {
    public int[] countBits(int num) {
        int[] dp = new int[num + 1];
        for (int $ = 1; $ != dp.length; ++$) dp[$] = dp[$ >> 1] + ($ & 1);
        return dp;          
    }
}
