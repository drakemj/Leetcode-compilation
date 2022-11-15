/*
    Given an input array, return array where the ith element is the product of all other elements in the input. Division not allowed.
*/

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> o(n, 1);
        int l = 1, r = 1;
        for (int i = 0; i < n-1; ++i){
            l *= nums[i];
            r *= nums[n-1-i];
            o[i+1] *= l;
            o[n-2-i] *= r;
        }
        return o;
    }
};