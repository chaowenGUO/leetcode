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
    int minDepth(TreeNode* root) {
        if (!root) return 0;
        else
        {
            auto const [min, max]{std::minmax({this->minDepth(root->left), this->minDepth(root->right)})};
            return 1 + (min ? min : max);
        }
    }
};
