class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        std::sort(std::begin(nums), std::end(nums));
        auto result{std::accumulate(std::cbegin(nums), std::next(std::cbegin(nums), 3), 0)};
        for (auto index{std::cbegin(nums)}; index != std::prev(std::cend(nums), 2);)
        {
            auto const num{*index};
            auto left{std::next(index)}, right{--std::cend(nums)};
            while (left != right)
            {
                auto const numsLeft{*left}, numsRight{*right};
                auto const total{num + numsLeft + numsRight};
                if (total == target) return target;
                if (total <= target) while (left != right && *left == numsLeft) ++left;
                if (total >= target) while (left != right && *right == numsRight) --right;
                if (std::abs(total - target) < std::abs(result - target)) result = total;
            }
            while (*index == num && index != std::prev(std::cend(nums), 2)) ++index;
        }
        return result;
    }
};
