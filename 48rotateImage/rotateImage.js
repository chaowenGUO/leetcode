/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    matrix.reverse()
    for (const row of Array(matrix.length).keys())
        for (let column = row + 1; !Object.is(column, matrix.length); ++column) [matrix[row][column], matrix[column][row]] = [matrix[column][row], matrix[row][column]]
};
