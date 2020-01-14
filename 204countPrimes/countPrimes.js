/**
 * @param {number} n
 * @return {number}
 */
var countPrimes = function(n) {
    if (n < 2) return 0
    else
    {
        const result = Array(n).fill(1)
        result[0] = result[1] = 0
        for (let i = 2; !Object.is(i, Math.trunc(Math.sqrt(n)) + 1); ++i)
            for (let j = i**2; j < n; j += i) result[j] = 0
        return result.reduce((a,b) => a + b)
    }
};
