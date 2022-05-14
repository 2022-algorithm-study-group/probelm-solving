class Solution {
public:
    string countAndSay(int n) {
        if(n == 1){
            return "1";
        }
        return count(countAndSay(n - 1));
    }
    
    string count(string target){
        string ret = "";
        char curr = target[0];
        int N = target.size();
        int cnt = 1;
        
        for(int i = 1; i < N; i++){
            if(curr == target[i]){
                cnt++;
            } else {
                ret += to_string(cnt);
                ret += curr;
                cnt = 1;
                curr = target[i];
            }
        }     
        
        ret += to_string(cnt);
        ret += curr;
        return ret;
    }
};
