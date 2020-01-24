class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        if (std::size(s1) + std::size(s2) != std::size(s3)) return false;
        else
        {
            std::vector<bool> dp(std::size(s2) + 1);
            dp.front() = true;
            for (std::size_t column{1}; column != std::size(dp); ++column) dp.at(column) = dp.at(column - 1) && s3.at(column - 1) == s2.at(column - 1);
            for (std::size_t row{1}; row != std::size(s1) + 1; ++row)
            {
                dp.front() = dp.front() && s3.at(row - 1) == s1.at(row - 1);
                for (std::size_t column{1}; column != std::size(dp); ++column) dp.at(column) = dp.at(column) && s3.at(row + column - 1) == s1.at(row - 1) || dp.at(column - 1) && s3.at(row + column - 1) == s2.at(column - 1);
            }
            return dp.back();
        }
    }
};
