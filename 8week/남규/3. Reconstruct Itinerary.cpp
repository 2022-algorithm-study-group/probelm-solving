// 방문한걸 체크하는게 아니라 모든 여행지를 방문할 수 있도록 변경해야함
class Solution {
public:
    unordered_set<string> visited;
    unordered_map<string, vector<string>> adj;
    int k;
    vector<string> ans;
    
    void dfs(string curr, vector<string> pAns){
        if(ans.size() == k){
            return;
        }
        
        if(pAns.size() == k){
            ans = pAns;
            return;
        }
        
        for(auto next : adj[curr]){
            if(visited.find(next) != visited.end()){
                continue;
            }
            visited.insert(next);
            pAns.push_back(next);
            dfs(next, pAns);
            visited.erase(next);
            pAns.pop_back();
        }
    }
    
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        for(auto ticket : tickets){
            string s = ticket[0];
            string d = ticket[1];
            adj[s].push_back(d);
            adj[d].push_back(s);
            sort(adj[s].begin(), adj[s].end());
            sort(adj[d].begin(), adj[d].end());
        }
        
        int k = adj.size();
        
        this->k = k;
        vector<string> pAns = {"JFK"};
        visited.insert("JFK");
        dfs("JFK", pAns);
        return ans;
    }
};
