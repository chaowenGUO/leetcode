/**
 * @param {string} s1
 * @param {string} s2
 * @param {string} s3
 * @return {boolean}
 */
var isInterleave = function(s1, s2, s3) {
    s1 = [...s1]
    s2 = [...s2]
    s3 = [...s3]
    if (!Object.is(s1.length + s2.length, s3.length)) return false
    else
    {
        const dp = [true, ...Array(s2.length).fill(false)]
        for (let column = 1; !Object.is(column, dp.length); ++column) dp[column] = dp[column - 1] && Object.is(s3[column - 1], s2[column - 1])
        for (let row  = 1; !Object.is(row, s1.length + 1); ++row)
        {
            dp[0] = dp[0] && Object.is(s3[row - 1], s1[row - 1])
            for (let column = 1; !Object.is(column, dp.length); ++column) dp[column] = dp[column] && Object.is(s3[row + column - 1], s1[row - 1]) || dp[column - 1] && Object.is(s3[row + column - 1], s2[column - 1])
        }
        return dp[dp.length - 1]
    }
};
