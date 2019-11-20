class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        auto index{std::empty(nums) ? 0 : 1};
        std::for_each(std::cbegin(nums), std::cend(nums), [&](auto const num){
            if (num > nums[index - 1])
            {
                nums[index] = num;
                ++index;
            }});
        return index;
    }
};
