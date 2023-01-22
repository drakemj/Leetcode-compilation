// Given an array, find the minimum start value that you can prepend the array with such that the cummulative total of the array is never less than 1 when
// evaluated left to right.

class Solution {
public:
    int minStartValue(vector<int>& nums) {
        int minVal = INT_MAX, sum = 0;
        for (int i : nums) {
            sum += i;
            minVal = min(minVal, sum);
        }
        return max(1 - minVal, 1);
    }
};