class Solution {
public:
    int maxArea(vector<int>& height) {
        auto left{std::cbegin(height)}, right{--std::cend(height)};
        std::size_t result{0};
        while (left != right)
        {
            result = std::max(result, static_cast<std::size_t>(right - left) * std::min(*left, *right));
            *left < *right ? ++left : --right;
        }
        return result;
    }
};
