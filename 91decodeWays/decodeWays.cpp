class Solution {
public:
    int numDecodings(string s) {
        if (s.front() == '0') return 0;
        else
        {
            auto a{1}, b{1}, c{0};
            for (std::size_t _{1}; _ != std::size(s); ++_)
            {
                if (s.at(_) != '0') c = b;
                auto const substr{s.substr(_ - 1, 2)};
                if ("10" <=  substr && substr <= "26") c += a;
                a = b;
                b = c;
                c = 0;
            }
            return b;
        }
    }
};
