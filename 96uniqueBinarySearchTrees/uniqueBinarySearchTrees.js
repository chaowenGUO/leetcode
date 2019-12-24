/**
 * @param {number} n
 * @return {number}
 */
var numTrees = function(n) {
    let catalan = 1
    for (let _ = 0; !Object.is(_, n); ++_) catalan = catalan * 2 * (2 * _ + 1) / (_ + 2)
    return catalan
};
