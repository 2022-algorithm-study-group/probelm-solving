class Solution {
public:
    vector<int> findOriginalArray(vector<int>& changed) {
        sort(changed.begin(), changed.end());
        unordered_map<int, int> umap;
        for(auto v : changed) {
            umap[v]++;
        }
        int N = changed.size();
        if(N % 2) return {};
        vector<int> ans;
        
        for(int i = 0; i < N; i++){
            if(umap[changed[i]] == 0) {
                continue;
            }
            umap[changed[i]]--;
            int doubleV = changed[i] * 2;
            
            if(umap[doubleV] == 0) {
                continue;
            } else {
                umap[doubleV]--;
                ans.push_back(changed[i]);
            }
        }
        if(ans.size() == N / 2) return ans;
        return {};
    }
};
