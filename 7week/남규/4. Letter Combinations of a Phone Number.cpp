class Solution {
public:
    unordered_map<char, vector<char>> digitToChars;
    vector<string> ans;
    
    void traverse(string& digits, int pos, string pAns){
        if(digits.size() == pos){
            ans.push_back(pAns);
            return;
        }
        
        for(char c : digitToChars[digits[pos]]){
            traverse(digits, pos + 1, pAns + c);
        }
    }
    
    
    vector<string> letterCombinations(string digits) {
        if(digits == "") return {};
        digitToChars['2'] = {'a', 'b', 'c'};
        digitToChars['3'] = {'d', 'e', 'f'};
        digitToChars['4'] = {'g', 'h', 'i'};
        digitToChars['5'] = {'j', 'k', 'l'};
        digitToChars['6'] = {'m', 'n', 'o'};
        digitToChars['7'] = {'p', 'q', 'r', 's'};
        digitToChars['8'] = {'t', 'u', 'v'};
        digitToChars['9'] = {'w', 'x', 'y', 'z'};
        traverse(digits, 0, "");
        return ans;
    }
};
