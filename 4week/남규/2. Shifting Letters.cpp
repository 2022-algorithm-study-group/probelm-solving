// https://leetcode.com/problems/shifting-letters/

class Solution {
public:
    string shiftingLetters(string s, vector<int>& shifts) {
        string ans = "";
        int race = 0;
        for(int i = shifts.size() - 1; i >= 0; i--){
            race += shifts[i];
            race %= 26;
            
            int t = (s[i] - 'a') + race;
            t %= 26;
            
            ans += ('a' + t);
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
