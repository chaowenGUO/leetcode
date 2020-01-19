/**
 * @param {number} num
 * @return {number[]}
 */
var countBits = function(num) {
    const dp = Array(num + 1).fill(0)
    for (let _ = 1; !Object.is(_, dp.length); ++_) dp[_] = dp[_ >> 1] + (_ & 1)
    return dp
};
