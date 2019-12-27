class Solution {
private:
    static constexpr auto even(int num)
    {
        auto result{0};
        while (num)
        {
            num /= 10;
            ++result;
        }
        return 1 - result & 1;
    }
public:
    int findNumbers(vector<int>& nums) {
        return std::accumulate(std::begin(nums), std::transform(std::cbegin(nums), std::cend(nums), std::begin(nums), this->even), 0);
    }
};
