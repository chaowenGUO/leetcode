/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    let result = 1
    for (let _ = 1; !Object.is(_, m); ++_) result = result * (n - 1 + _) /_
    return result
};
