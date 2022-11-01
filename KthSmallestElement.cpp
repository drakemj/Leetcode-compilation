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
            out = kthSmallest(root->left, k);                       //continue left to reach the smallest.
            if (out >= 0) return out;                               //out returns a negative value corresponding to the amount of smallest nodes checked.
            if (out + k == 1) return root->val;                     //once control returns here, can check this node, else go right.
        }
        if (k == 1) return root->val;                               //right side can cause k to equal 1.
        if (root->right){
            int t = kthSmallest(root->right, k + out - 1);          //must immediately check for left nodes first, keep track of out accumulated from left
            if (t > 0) return t;
            out += t;
        }
        return out-1;                                               //return control to node if left and right have been checked, pass out
    }

};