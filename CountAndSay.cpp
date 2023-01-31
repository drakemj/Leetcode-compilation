class Solution {
public:
    string countAndSay(int n) {
        if (n == 1) return "1";
        string s = countAndSay(n - 1);
        string o;
        int p = 0;
        while (p < s.length()) {
            int count = 1;
            char c = s[p];
            while (s[++p] == c) count++;
            o += count + 48;
            o += c;
        }
        return o;
    }
};