class Solution {
public:
    int minDistance(string word1, string word2) {
        std::vector<int> dp(std::size(word2) + 1);
        std::iota(std::begin(dp), std::end(dp), 0);
        for (std::size_t row{1}; row != std::size(word1) + 1; ++row)
        {
            auto const prev{dp};
            dp.front() = row;
            for (std::size_t column{1}; column != std::size(dp); ++column)
            {
                std::vector<double> const min{dp.at(column - 1) + 1, prev.at(column - 1) + 1, prev.at(column) + 1, word1.at(row - 1) == word2.at(column - 1) ? prev.at(column - 1) : std::numeric_limits<double>::infinity()};
                dp.at(column) = *std::min_element(std::cbegin(min), std::cend(min));
                
            }
        }
        return dp.back();
    }
};
