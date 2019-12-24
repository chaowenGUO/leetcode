class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        std::reverse(std::begin(matrix), std::end(matrix));
        for (std::size_t row{}; row != std::size(matrix); ++row)
            for (std::size_t column{row + 1}; column != std::size(matrix); ++column) std::swap(matrix.at(row).at(column), matrix.at(column).at(row));
    }
};
