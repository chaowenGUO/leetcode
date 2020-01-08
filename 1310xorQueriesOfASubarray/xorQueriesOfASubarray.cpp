class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        std::partial_sum(std::cbegin(arr), std::cend(arr), std::begin(arr), std::bit_xor{});
        std::vector<int> result(std::size(queries));
        std::transform(std::cbegin(queries), std::cend(queries), std::begin(result), [&arr = std::as_const(arr)](auto const _){
            return _.front() ? arr.at(_.front() - 1) ^ arr.at(_.back()) : arr.at(_.back());});
        return result;
    }
};
