class Solution {
public:
    int maxArea(vector<int>& height) {
        auto left{std::cbegin(height)}, right{--std::cend(height)};
        auto result{0};
        while (left != right)
        {
            result = std::max<std::size_t>(result, std::distance(left, right) * std::min(*left, *right));
            *left < *right ? ++left : --right;
        }
        return result;
    }
};
