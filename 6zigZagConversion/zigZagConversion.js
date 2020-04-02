/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    if (Object.is(numRows, 1)) return s
    else
    {
        const result = Array(numRows).fill('')
        let row = 0, direction = 1
        for (const _ of s)
        {
            result[row] += _
            if (Object.is(row, 0)) direction = 1
            else if (Object.is(row, numRows - 1)) direction = -1
            row += direction
        }
        return result.join('')
    }
};
