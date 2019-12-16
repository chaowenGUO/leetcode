class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        auto const range{std::equal_range(std::cbegin(nums), std::cend(nums), target)};
        return range.first != range.second ? std::vector<int>{std::distance(std::cbegin(nums), range.first), std::distance(std::cbegin(nums), range.second) - 1} : std::vector<int>(2, -1); 
    }
};
