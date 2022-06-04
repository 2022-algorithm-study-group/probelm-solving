class Solution {
public:
    unordered_map<string, int> cache;
    unordered_set<string> wordSet;
    int getStrChain(string word){
        if(cache.find(word) != cache.end()){
            return cache[word];
        }
        int &ret = cache[word];
        ret = 1;
        
        for(int i = 0; i < word.size(); i++){
            string next = word.substr(0, i) + word.substr(i + 1);
            if(wordSet.find(next) == wordSet.end()){
                continue;
            }
            ret = max(ret, getStrChain(next) + 1);
        }
        return ret;
    }
    
    int longestStrChain(vector<string>& words) {
        int ans = 0;
        
        for(auto word : words){
            wordSet.insert(word);
        }
        
        for(auto word : words){
            ans = max(ans, getStrChain(word));
        }
        return ans;
    }
};
