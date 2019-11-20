class Solution {
public:
    int trap(vector<int>& height) {
        auto [result, level]{std::array<int, 2>{}};
        if (std::empty(height)) return result;
        auto left{std::cbegin(height)}, right{--std::cend(height)};
        while (left != right)
        {
            auto const low = std::min(*left, *right);
            *left < *right ? ++left : --right;
            level = std::max(level, low);
            result += level - low;
        }
        return result;
    }
};
