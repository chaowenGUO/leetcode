/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int deepestLeavesSum(TreeNode* root) {
        std::vector<int> result;
        std::vector level{root};
        while (root && !std::empty(level))
        {
            result.clear();
            std::transform(std::cbegin(level), std::cend(level), std::back_inserter(result), [](auto const node){return node->val;});
            decltype(level) newLevel;
            std::for_each(std::cbegin(level), std::cend(level), [&newLevel](auto const node){
                if (node->left) newLevel.emplace_back(node->left);
                if (node->right) newLevel.emplace_back(node->right);});
            level = std::move(newLevel);
        }
        return std::accumulate(std::cbegin(result), std::cend(result), 0);
    }
};
