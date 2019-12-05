class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        std::vector<std::vector<int>> result;
        std::sort(std::begin(intervals), std::end(intervals), [](auto const a, auto const b){return a.front() < b.front();});
        for (auto const& interval: intervals)
        {
            if (!std::empty(result) && interval.front() <= result.back().back()) result.back().back() = std::max(result.back().back(), interval.back());
            else result.emplace_back(interval);
        }
        return result;
    }
};
