/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 * 
 * Find the maximum cumulative total along an interupted path in a binary tree. Each edge can only be visited once.
 */
class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int o = INT_MIN;
        maxPath(root, o);
        return o;
    }

    int maxPath(TreeNode* root, int& m){
        if (!root) return 0;
        int l = maxPath(root->left, m);             // find max left, right
        int r = maxPath(root->right, m);
        int t = max(l, r);                          // need to calculate the greater child
        m = max(m, l+r+root->val);                  // if this root is "connecting" left and right paths
        if (root->val > t+root->val){
            m = max(m, root->val);                  // if root is larger than sum with greater child, pass root
            return root->val;                       // (largest path will not include a path that makes value smaller)
        }
        m = max(m, t+root->val);                    // o/w pass value of greatest path including the root
        return t + root->val;
    }
};