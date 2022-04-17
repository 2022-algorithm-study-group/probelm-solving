// https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

class Solution {
public:
    vector<int> findNumOfValidWords(vector<string>& words, vector<string>& puzzles) {
        unordered_map<int, int> freqs;
        
        for(auto word : words){
            int cand = 0;
            for(int i = 0; i < word.size(); i++){
                cand |= (1 << (word[i] - 'a'));
            }
            freqs[cand]++;
        }
        
        vector<int> ans;
        
        for(auto puzzle : puzzles){
            int firstChar = (1 << (puzzle[0] - 'a'));
            int mask = 0;
            for(int i = 1; i < puzzle.size(); i++){
                mask |= (1 << (puzzle[i] - 'a'));
            }
            
            int cnt = freqs[firstChar];
            
            for(int submask = mask; submask; submask = (submask - 1) & mask){
                cnt += freqs[submask | firstChar];
            }
            ans.push_back(cnt);
        }
        return ans;
    }
};
