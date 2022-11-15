class Solution {
public:
    int n;
    void rotate(vector<vector<int>>& matrix) {
        n = matrix.size();
        for (int i = 0; i < n/2; ++i)
            for (int j = 0; j < n/2 + (n&1); ++j){
                swap(matrix, i, j);
            }
    }

    void swap(vector<vector<int>>& m, int i, int j){
        int select[] = {j, n-1-i, n-1-j, i, j};
        int t = m[i][j];
        for (int x = 0; x < 4; ++x){
            int a = select[x], b = select[x+1];
            int temp = m[a][b];
            m[a][b] = t; 
            t = temp;
        }
    }
};