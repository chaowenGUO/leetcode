class Solution {
public:
    int maxArea(vector<int>& height) {
        auto left{std::cbegin(height)}, right{std::prev(std::cend(height))};
        auto result{0};
        while (left < right)
        {
            result = std::fmax(result, std::distance(left, right) * std::min(*left, *right));
            *left < *right ? std::advance(left, 1) : std::advance(right, -1);
        }
        return result;
    }
};
