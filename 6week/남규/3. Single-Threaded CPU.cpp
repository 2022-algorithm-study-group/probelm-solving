class Solution {
public:
    vector<int> getOrder(vector<vector<int>>& tasks) {
        priority_queue<vector<int>> pq;
        int N = tasks.size();
        vector<int> ans;
        
        for(int i = 0; i < N; i++){
            tasks[i].push_back(i);
        }
        
        sort(tasks.begin(), tasks.end());
        int curr = 1;
        pq.push({-tasks[0][1], -tasks[0][2]});
        long long time = tasks[0][0];
        
        while(!pq.empty()){
            int processingTime = -pq.top()[0];
            int index = -pq.top()[1];
            pq.pop();
            
            time += processingTime;
            
            while(curr < N){
                if(tasks[curr][0] <= time){
                    pq.push({-tasks[curr][1], -tasks[curr][2]});
                } else {
                    break;
                }
                curr++;
            }
            
            if(pq.empty() && curr < N){
                time = tasks[curr][0];
                pq.push({-tasks[curr][1], -tasks[curr][2]});
                curr++;
            }
            
            ans.push_back(index);
        }
        return ans;
    }
};
