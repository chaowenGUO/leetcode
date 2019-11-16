class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, std::size_t> dictionary;
        for (auto iter{std::cbegin(nums)};;++iter)
        {
            auto const index{std::distance(std::cbegin(nums), iter)};
            if (auto find{dictionary.find(*iter)}; find != std::cend(dictionary)) return {index, find->second};
            else dictionary.try_emplace(target - *iter, index);
        }
    }
};
