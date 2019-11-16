class Solution {
public:
    vector<string> generateParenthesis(int n) {
        std::vector<std::vector<std::string>> dp(n + 1);
        dp.front().resize(1);
        for (auto i{0}; i != n + 1; ++i)
            for (auto j{0}; j != i; ++j)
                for (auto const x: dp.at(j))
                     for (auto const y: dp.at(i - j - 1)) dp.at(i).emplace_back("(" + x + ")" + y);
        return dp.back();
    }
};
