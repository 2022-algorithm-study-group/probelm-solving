class Solution {
public:
    int cache[21][32];
    
    int traverse(string &s, string &p, int i, int j, int n, int m){
        if(i == n && j == m){
            return true;
        }
        
        int &ret = cache[i][j];
        if(ret != -1) return ret;
        ret = 0;
        bool firstMatch = (i < n && (s[i] == p[j] || p[j] == '.'));
        
        if(j + 1 < m && p[j + 1] == '*'){
            ret |= traverse(s, p, i, j + 2, n, m);
            if(firstMatch)
                ret |= traverse(s, p, i + 1, j, n, m);
        } else {
            if(firstMatch)
                ret |= traverse(s, p, i + 1, j + 1, n, m);
        }
        return ret;
    }
    
    bool isMatch(string s, string p) {
        memset(cache, -1, sizeof(cache));
        return traverse(s, p, 0, 0, s.size(), p.size());
    }
};
