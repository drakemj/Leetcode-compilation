/*
Take an mxn array and transform it into a spiral matrix. See https://leetcode.com/problems/spiral-matrix/description/
*/
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> d = {0, 1, 0, -1, 0};                           // indexing this array will give the directions right, down, left, up
        vector<int> o;
        int current = 0, count = 0;
        int m = matrix.size(), n = matrix[0].size(), x = 0, y = 0;
        vector<int> l = {0, 1, n-1, -1, m-1, -1, 0, 1};             // comes in pairs, first is the limit, second is the direction
        bool hv = false;                                            // flag to keep track of which element is to be limited

        while (count++ < m*n){
            o.push_back(matrix[x][y]);
            int lim;
            if (hv){
                lim = x;
            }
            else {
                lim = y;
            }
            if (lim == l[((current + 1) % 4) * 2]) {                // if reaches the according limit
                l[current * 2] += l[current * 2 + 1];               // increment previous limit according to its direction
                current = (current + 1) % 4;                        // and update current and hv.
                hv = !hv;                                           
            }
            x += d[current];                                        // directional increment
            y += d[current + 1];
        }
        return o;
    }
};