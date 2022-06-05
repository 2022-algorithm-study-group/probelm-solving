class Solution {
public:
    bool canConvert(string str1, string str2) {
        if(str1 == str2) return true;
        
        unordered_map<char, char> appeared;
        unordered_set<char> uset;
        
        int n = str1.size();
        
        for(int i = 0; i < n; i++){
            char c1 = str1[i];
            char c2 = str2[i];
            
            if(appeared.find(c1) == appeared.end()){
                appeared[c1] = c2;
                uset.insert(c2);
            } else if(appeared[c1] != c2){
                return false;
            }
            
            
        }
        if(uset.size() < 26){
            return true;
        }
        return false;
    }
};
