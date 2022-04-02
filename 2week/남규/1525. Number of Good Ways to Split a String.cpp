class Solution {
public:
    int numSplits(string s) {
        /* 
        TC1
        s = "aacaca"
        ways = {{"aac", "aca"}, {"aaca", "ca"}}
        
        TC2
        s = "abacda"
        ways: "Empty"
        
        approach
        
        1. count characters into map, {'a': 4, 'c': 2}
        2. Remove chracter's count from map by iterating left of s to right
        
        "aacaca"
        
        rightDistinct = 2;
        countRight = {'a': 4, 'c': 2}
        countLeft = {}
        
        for(int i = 0; i < s.size(); i++){
            char c = s[i];
            countLeft[c]--;
            
            if(countLeft[c] == 0){
                rightDistinct--;
            }
            
            if(countRight[c] == 0){
                leftDisinct++;
            }
            countRight[c]++;
            
            if(rightDistinct == leftDistinct) ans++;
        }
        return ans;
        
        Time Complexity: O(N)
        Space Complexity: O(N)
        */
        
        unordered_map<char, int> countLeft;
        unordered_map<char, int> countRight;
        int leftDistinct = 0, rightDistinct = 0;
        
        int N = s.size();
        
        for(int i = 0; i < N; i++){
            char c = s[i];
            if(countRight[c] == 0){
                rightDistinct++;
            }
            countRight[c]++;
        }
        
        int ans = 0;
        
        // 0 ~ N - 1 / N<=i
        for(int i = 0; i < N - 1; i++){
            char c = s[i];
            
            if(countLeft[c] == 0){
                leftDistinct++;
            }
            countLeft[c]++;
            
            countRight[c]--;
            if(countRight[c] == 0){
                rightDistinct--;
            }
            
            if(rightDistinct == leftDistinct) ans++;
        }
        return ans;
    }
};
