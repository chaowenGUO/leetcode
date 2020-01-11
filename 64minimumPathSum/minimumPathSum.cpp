class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        auto dp{grid.front()};
        std::partial_sum(std::cbegin(dp), std::cend(dp), std::begin(dp));
        std::for_each(++std::cbegin(grid), std::cend(grid), [&dp](auto const row){
            dp.front() += row.front();
            for (std::size_t column{1}; column != std::size(row); ++column) dp.at(column) = std::min(dp.at(column - 1), dp.at(column)) + row.at(column);});
        return dp.back();
    }
};
