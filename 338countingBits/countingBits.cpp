class Solution {
public:
    vector<int> countBits(int num) {
        std::invoke_result_t<decltype(&Solution::countBits), Solution, decltype(num)> dp(num + 1);
        for (std::size_t _{1}; _ != std::size(dp); ++_) dp.at(_) = dp.at(_ >> 1) + (_ & 1);
        return dp;
    }
};
