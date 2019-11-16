class Solution {
public:
    int maxArea(vector<int>& height) {
        auto [left, right]{std::pair{std::size_t{0}, std::size(height) - 1}};
        std::size_t result{0};
        while (left < right)
        {
            result = std::max(result, (right - left) * std::min(height[left], height[right]));
            height[left] < height[right] ? ++left : --right;
        }
        return result;
    }
};
