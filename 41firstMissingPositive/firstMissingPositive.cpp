class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        for (std::size_t index{0}; index != std::size(nums); ++index)
            while (0 <= nums.at(index) - 1 && nums.at(index) - 1 < std::size(nums) && nums.at(nums.at(index) - 1) != nums.at(index)) std::swap(nums.at(nums.at(index) - 1), nums.at(index));
        for (std::size_t index{0}; index != std::size(nums); ++index)
            if (nums.at(index) != index + 1) return index + 1;
        return std::size(nums) + 1;
    }
};
