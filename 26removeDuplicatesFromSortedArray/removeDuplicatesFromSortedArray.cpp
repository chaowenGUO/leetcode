class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        auto index{nums.empty() ? 0 : 1};
        for (auto const num: nums)
        {
            if (num > nums[index - 1])
            {
                nums[index] = num;
                ++index;
            }
        }
        return index;
    }
};
