/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    const Roman = Object.freeze([['M', 1000], ['CM', 900], ['D', 500], ['CD', 400], ['C', 100], ['XC', 90], ['L', 50], ['XL', 40], ['X', 10], ['IX', 9], ['V', 5], ['IV', 4], ['I', 1]])
    const result = []
    Roman.forEach(([symbol,value]) => {
        result.push(symbol.repeat(num / value))
        num %= value})
    return result.join('')
};
