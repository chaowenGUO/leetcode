class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::vector<std::vector<int>> result;
        if (std::size(nums) < 3) return result;
        std::sort(std::begin(nums), std::end(nums));
        for (auto index{0ul}; index != std::size(nums) - 2;)
        {
            auto const num{nums.at(index)};
            if (num > 0) break;
            auto [left, right]{std::pair{index + 1, std::size(nums) - 1}};
            while (left < right)
            {
                auto const [numsLeft, numsRight]{std::pair{nums.at(left), nums.at(right)}};
                auto const total{num + numsLeft + numsRight};
                if (total == 0) result.emplace_back(std::vector{num, numsLeft, numsRight});
                if (total <= 0) while (left < right && nums.at(left) == numsLeft) ++left;
                if (total >= 0) while (left < right && nums.at(right) == numsRight) --right;
            }
            while (num == nums.at(index) && index != std::size(nums) - 2) ++index;
        }
        return result;
    }
};
