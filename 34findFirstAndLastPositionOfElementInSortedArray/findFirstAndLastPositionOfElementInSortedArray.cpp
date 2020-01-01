class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        auto const [left, right]{std::equal_range(std::cbegin(nums), std::cend(nums), target)};
        using type = std::invoke_result_t<decltype(&Solution::searchRange), Solution, decltype(nums), decltype(target)>;
        return left != right ? type{std::distance(std::cbegin(nums), left), std::distance(std::cbegin(nums), right) - 1} : type(2, -1);
    }
};
