class Solution {
public:
    string expandFreq(string target){
        string ret = "";
        int left = 0;
        int right = 0;
        int T = target.size();
        
        while(left <= right && right < T){
            if(target[left] == target[right]){
                right++;
                continue;
            }
            ret += ('0' + (right - left));
            ret += target[left];
            left = right;
        }
        
        if(left < right){
            ret += ('0' + (right - left));
            ret += target[left];
        }
        return ret;
    }
    
    string countAndSay(int n) {
        if(n == 1){
            return "1";
        }
        
        return expandFreq(countAndSay(n - 1));
    }
};
