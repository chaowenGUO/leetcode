class Solution {
public:
    bool isMatch(string s, string p) {
        std::vector<bool> dp(std::size(p) + 1);
        dp.front() = true;
        for (std::size_t column{1}; column != std::size(dp); ++column) dp.at(column) = dp.at(column - 1) && p.at(column - 1) == '*';
        for (std::size_t row{1}; row != std::size(s) + 1; ++row)
        {
            auto const prev{dp};
            dp.front() = false;
            for (std::size_t column{1}; column != std::size(dp); ++column)
            {
                if (s.at(row - 1) == p.at(column - 1) || p.at(column - 1) == '?') dp.at(column) = prev.at(column - 1);
                else if (p.at(column - 1) == '*') dp.at(column) = dp.at(column - 1) || prev.at(column);
                else dp.at(column) = false;
            }
        }
        return dp.back();
    }
};
