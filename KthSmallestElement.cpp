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
 * 
 * This code just finds the kth smallest element in a binary tree. I tried to constrain myself by just using the return value to pass
 * information in between calls.
 */

class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        int out = 0;
        if (root->left) {
            out = kthSmallest(root->left, k);
            if (out >= 0) return out;
            if (out + k == 1) return root->val;
        }
        if (k == 1) return root->val;
        if (root->right){
            int t = kthSmallest(root->right, k + out - 1);
            if (t > 0) return t;
            out += t;
        }
        return out-1;
    }

};