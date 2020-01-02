class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        std::vector<std::string> seen;
        for (std::size_t row{}; row != std::size(board); ++row)
            for (std::size_t column{}; column != std::size(board.at(row)); ++column)
                if (auto const element{board.at(row).at(column)}; element != '.') seen.insert(std::cend(seen), {element + ")"s + std::to_string(column), std::to_string(row) + "(" + element, std::to_string(row / 3) + "(" + element + ")" + std::to_string(column / 3)});
        return std::size(seen) == std::size(std::unordered_set(std::cbegin(seen), std::cend(seen)));
    }
};
