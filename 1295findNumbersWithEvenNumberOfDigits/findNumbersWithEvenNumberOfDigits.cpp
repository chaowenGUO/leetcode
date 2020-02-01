class Solution {
public:
    int findNumbers(vector<int>& nums) {
        return std::count(std::begin(nums), std::transform(std::cbegin(nums), std::cend(nums), std::begin(nums), [](auto const num){return 1 - std::size(std::to_string(num)) & 1;}), 1);
    }
};
