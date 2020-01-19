/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    s = [...s]
    p = [...p]
    let dp = [true, ...Array(p.length).fill(false)]
    for (let column = 1; !Object.is(column, dp.length); ++column)
        if (Object.is(p[column - 1], '*')) dp[column] = dp[column - 1]
    let prev = [...dp]
    for (let row = 1; !Object.is(row, s.length + 1); ++row)
    {
        dp[0] = false
        for (let column = 1; !Object.is(column , dp.length); ++column)
        {
            if (Object.is(s[row - 1], p[column - 1]) || Object.is(p[column - 1], '?')) dp[column] = prev[column - 1]
            else if (Object.is(p[column - 1], '*')) dp[column] = dp[column - 1] || prev[column]
            else dp[column] = false
        }
        [prev, dp] = [dp, prev]
    }
    return prev[prev.length - 1]
};
