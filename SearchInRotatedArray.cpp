/*
Take sorted array that might be pivoted around a point and find the target in O(log n) time.
Rotated at k = 5: [5, 6, 7, 0, 1, 2, 3, 4]    
*/

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        while (l <= r){
            int m = (l + r)/2;
            if (nums[m] == target) return m;
            if (nums[m] < target){
                if (nums[r] < target && nums[m] <= nums[r]) r = m - 1;
                else l = m + 1;
            } 
            else {
                if (nums[l] > target && nums[m] >= nums[l]) l = m + 1;
                else r = m - 1;
            }
        }
        return -1;
    }
};