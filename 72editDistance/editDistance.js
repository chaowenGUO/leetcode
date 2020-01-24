/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function(word1, word2) {
    word1 = [...word1]
    word2 = [...word2]
    let dp = [...Array(word2.length + 1).keys()]
    for (let row = 1; !Object.is(row, word1.length + 1); ++row)
    {
        prev = [...dp]
        dp[0] = row
        for (let column = 1; !Object.is(column, dp.length); ++column) dp[column] = Math.min(dp[column - 1] + 1, prev[column] + 1, prev[column - 1] + 1, Object.is(word1[row - 1], word2[column - 1]) ? prev[column - 1] : Infinity);
    }
    return dp[dp.length - 1]
};
