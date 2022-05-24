class Solution {
public:
    int ticketCount = 0;
    unordered_map<string, unordered_map<string, int>> fromTo;
    unordered_map<string, vector<string>> adj;
    
    vector<string> ans;
    
    void dfs(string from, vector<string>& path){
        if(ans.size() != 0) return;
        
        if(ticketCount == 0){
            ans = path;
            return;
        }
        
        for(int i = 0; i < adj[from].size(); i++){
            string &to = adj[from][i];
            if(fromTo[from][to] > 0){
                path.push_back(to);
                fromTo[from][to]--;
                ticketCount--;
                dfs(to, path);
                fromTo[from][to]++;
                ticketCount++;
                path.pop_back();
            }
        }
    }
    
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        for(int i = 0; i < tickets.size(); i++){
            if(tickets[i][0] == tickets[i][1]) continue;
            fromTo[tickets[i][0]][tickets[i][1]]++;
            adj[tickets[i][0]].push_back(tickets[i][1]);
            ticketCount++;
        }
        
        for(auto &v : adj){
            sort(v.second.begin(), v.second.end());
        }

        vector<string> path = {"JFK"};
        dfs("JFK", path);
        return ans;
    }
};
