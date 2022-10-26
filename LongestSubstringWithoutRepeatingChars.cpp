/*self explanatory.*/

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0, o = 0;
        unordered_map<char, int> m;
        for (int i = 0; i < s.length(); ++i){
            int t = -1;
            if (m.find(s[i]) != m.end()) t = m[s[i]];
            m[s[i]] = i;
            l = max(l, t + 1);
            o = max(o, i-l+1);
        }
        return o;
    }
};