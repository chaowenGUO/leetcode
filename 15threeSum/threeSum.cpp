class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::invoke_result_t<decltype(&Solution::threeSum), Solution, decltype(nums)> result;
        std::sort(std::begin(nums), std::end(nums));
        if (std::size(nums) < 3) return result;
        for (auto index{std::cbegin(nums)}; index != std::prev(std::cend(nums), 2);)
        {
            const auto num{*index};
            if (*index > 0) break;
            auto left{std::next(index)}, right{--std::cend(nums)};
            while (left != right)
            {
                const auto numsLeft{*left}, numsRight{*right};
                const auto total{num + numsLeft + numsRight};
                if (total == 0) result.emplace_back(std::vector{num, numsLeft, numsRight});
                if (total <= 0) while (left != right and numsLeft == *left) ++left;
                if (total >= 0) while (left != right and numsRight == *right) --right;
            }
            while (num == *index && index != std::prev(std::cend(nums), 2)) ++index;
        }
        return result;
    }
};
