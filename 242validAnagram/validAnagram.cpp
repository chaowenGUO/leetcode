class Solution {
private:
    static auto groupBy(std::string const s)
    {
        auto const utf32{std::wstring_convert<std::codecvt_utf8<char32_t>, char32_t>{}.from_bytes(s)};
        return std::unordered_multiset(std::cbegin(utf32), std::cend(utf32));
    }
    
public:
    bool isAnagram(std::string s, std::string t) {
        return this->groupBy(s) == this->groupBy(t);
    }
};
