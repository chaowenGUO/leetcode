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
        std::vector<decltype(std::declval<TreeNode>().val)> result;
        std::vector level{root};
        while (root && !std::empty(level))
        {
            std::vector<decltype(std::declval<TreeNode>().val)> value(std::size(level));
            std::transform(std::cbegin(level), std::cend(level), std::begin(value), [](auto const node){return node->val;});
            result = std::move(value);
            std::vector<decltype(root)> nodes;
            std::for_each(std::cbegin(level), std::cend(level), [&](auto const node){
                if (node->left) nodes.emplace_back(node->left);
                if (node->right) nodes.emplace_back(node->right);});
            level = std::move(nodes);
        }
        return std::accumulate(std::cbegin(result), std::cend(result), 0);
    }
};
