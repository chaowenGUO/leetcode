class Solution {
public:
    bool isValid(string s) {
        std::unordered_map const parentheses{std::pair{'{','}'}, {'[',']'}, {'(',')'}};
        std::stack<char> stack;
        for (auto const _: s)
            if (auto find{parentheses.find(_)}; find != std::cend(parentheses)) stack.emplace(find->second);
            else if (std::empty(stack) || stack.top() != _) return false;
            else stack.pop();
        return std::empty(stack);
    }
};
