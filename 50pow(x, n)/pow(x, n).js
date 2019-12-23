/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    let result = 1
    const sign = Math.sign(n)
    while (n)
    {
        if (n & 1) result *= x
        x *= x
        n = Math.trunc(n / 2)
    }
    return Object.is(sign, 1) ? result : 1 / result
};
