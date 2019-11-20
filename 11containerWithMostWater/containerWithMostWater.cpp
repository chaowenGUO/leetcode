class Solution {
public:
    int maxArea(vector<int>& height) {
        auto left{std::cbegin(height)}, right{--std::cend(height)};
        std::ptrdiff_t result{0};
        while (left < right)
        {
            result = std::max(result, std::distance(left, right) * std::min(*left, *right));
            *left < *right ? ++left : --right;
        }
        return result;
    }
};
