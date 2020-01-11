class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        std::vector<unsigned> dp(std::cbegin(obstacleGrid.front()), std::cend(obstacleGrid.front()));
        std::transform(std::cbegin(dp), std::cend(dp), std::begin(dp), [](auto const _){return 1 - _;});
        std::partial_sum(std::cbegin(dp), std::cend(dp), std::begin(dp), std::multiplies{});
        std::for_each(std::next(std::cbegin(obstacleGrid)), std::cend(obstacleGrid), [&dp](auto const row){
            dp.front() *= 1 - row.front();
            for (std::size_t column{1}; column != std::size(row); ++column) dp.at(column) = (dp.at(column - 1) + dp.at(column)) * (1 - row.at(column));});
        return dp.back();
    }
};
