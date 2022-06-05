class Solution {
public:
    string minWindow(string s1, string s2) {
        if(s1.size() < s2.size()){
            return "";
        }
        
        if(s1 == s2){
            return s1;
        }
        
        char start = s2[0];
        string ans = "";
        
        for(int i = 0; i < s1.size() - s2.size() + 1; i++){
            if(s1[i] == start){
                int j = i;
                int base = 0;
                for(; base < s2.size(); base++){
                    if(j == s1.size()) break;
                    
                    while(j < s1.size() && s1[j] != s2[base]){
                        j++;
                    }
                    
                    if(s1[j] == s2[base]){
                        j++;
                    } else {
                        break;
                    }
                }
                
                if(base == s2.size()){
                    string s = s1.substr(i, j - i);
                    if(ans == ""){
                        ans = s;
                    } else if(ans.size() > s.size()){
                        ans = s;
                    }
                }
            }
        }
        return ans;
    }
};
