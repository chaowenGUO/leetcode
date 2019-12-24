class Solution {
public:
    int numTrees(int n) {
        auto catalan{1};
        for (std::size_t _{}; _ != n; ++_) catalan = catalan * 2 * (2 * _ + 1) / (_ + 2);
        return catalan;
    }
};
