/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    let result = Array(2).fill(1)
    for (let _ = 0; _ != n; ++_) result = [result[1], result.reduce((a,b) => a + b)]
    return result[0]
};
