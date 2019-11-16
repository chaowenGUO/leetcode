class Solution {
public:
    string intToRoman(int num) {
        std::vector const Roman{std::pair{"M", 1000}, {"CM", 900}, {"D", 500}, {"CD", 400}, {"C", 100}, {"XC", 90}, {"L", 50}, {"XL", 40}, {"X", 10}, {"IX", 9}, {"V", 5}, {"IV", 4}, {"I", 1}};
        std::vector<std::string> result;
        std::for_each(std::cbegin(Roman), std::cend(Roman), [&num, &result](auto const _){
            auto const [symbol, value]{_};
            for (auto index{0}; index != num / value; ++index) result.emplace_back(symbol);
            num %= value;});
        std::stringstream stream;
        std::copy(std::cbegin(result), std::cend(result), std::ostream_iterator<std::string>{stream});
        return stream.str();
    }
};
