class Solution {
public:
    bool checkRecord(string s) {
        int absent = 0;
        int lateConsecutive = 0;
        
        for(int i = 0; i < s.size(); i++){
            if(s[i] == 'A') absent++;
            
            if(i > 0 && s[i] == 'L' && s[i] == s[i - 1]){
                lateConsecutive++;
                if(lateConsecutive == 2){
                    return false;
                }
            } else {
                lateConsecutive = 0;
            }
        }
        
        return absent >= 2 ? false : true;
    }
};
