/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let result = 0
    while (x)
        if (Math.abs(result) > ((1n << 31n) - 1n) / 10n) return 0
        else
        {
            result = result * 10 + x % 10
            x = Math.trunc(x / 10)
        }
    return result
};
