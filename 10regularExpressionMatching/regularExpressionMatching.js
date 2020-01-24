/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    s = [...s]
    p = [...p]
    let dp = [true, ...Array(p.length).fill(false)]
    for (let column = 2; column < dp.length; ++column) dp[column] = dp[column - 2] && Object.is(p[column - 1], '*')
    for (let row = 1; !Object.is(row, s.length + 1); ++row)
    {
        let prev = [...dp]
        dp[0] = false
        for (let column = 1; !Object.is(column, dp.length); ++column)
        {
            if (Object.is(s[row - 1], p[column - 1]) || Object.is(p[column - 1], '.')) dp[column] = prev[column - 1]
            else if (Object.is(p[column - 1], '*')) dp[column] = dp[column - 2] || prev[column] && (Object.is(s[row - 1], p[column - 2]) || Object.is(p[column - 2], '.'))
            else dp[column] = false
        }
    }
    return dp[dp.length - 1]
};
