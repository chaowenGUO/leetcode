class Solution {
public:
    int romanToInt(string s) {
        std::unordered_map const roman{std::pair{'M', 1000}, {'D', 500}, {'C', 100}, {'L', 50}, {'X', 10}, {'V', 5}, {'I', 1}};
        return std::accumulate(std::crbegin(s), std::crend(s), std::pair{0, 'I'}, [&roman = std::as_const(roman)](auto const result, auto const _){
            return std::pair{roman.at(_) < roman.at(result.second) ? result.first - roman.at(_) : result.first + roman.at(_), _};}).first;
    }
};
