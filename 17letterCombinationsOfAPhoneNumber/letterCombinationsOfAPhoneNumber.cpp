class Solution {
public:
    vector<string> letterCombinations(string digits) {
        std::unordered_map const phone{std::pair{2, "abc"}, {3, "def"}, {4, "ghi"}, {5, "jkl"}, {6, "mno"}, {7, "pqrs"}, {8, "tuv"}, {9, "wxyz"}};
        using type = std::invoke_result_t<decltype(&Solution::letterCombinations), Solution, decltype(digits)>;
        return std::empty(digits) ? type{} : std::accumulate(std::cbegin(digits), std::cend(digits), type(1) ,[&phone = std::as_const(phone)](auto const result, auto const digit){
            type out;
            for (auto const x: result)
                for (auto const y: std::string_view(phone.at(digit - '0'))) out.emplace_back(x + y);
            return out;});
    }
};
