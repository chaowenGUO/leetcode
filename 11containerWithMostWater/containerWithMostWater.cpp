class Solution {
public:
    int maxArea(vector<int>& height) {
        auto left{std::cbegin(height)}, right{--std::cend(height)};
        std::size_t result{};
        while (left != right)
        {
            result = std::max(result, static_cast<std::size_t>(std::distance(left, right) * std::min(*left, *right)));
            *left < *right ? ++left : --right;
        }
        return result;
    }
};
