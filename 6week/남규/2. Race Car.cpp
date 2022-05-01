class Solution {
public:
    int racecar(int target) {
        /*
        Time Complexity: O(log N), target == N
        Space Complexity: O(2^N) - worst
        
        */
        
        queue<vector<long long>> que;
        que.push({0, 1, 0}); // position, speed, steps
        int ans = 0;
        
        while(!que.empty()){
            long long position = que.front()[0];
            long long speed = que.front()[1];
            long long steps = que.front()[2];
            que.pop();
            
            if(position == target){
                ans = steps;
                break;
            }
            
            que.push({position + speed, speed * 2, steps + 1});
            if(position + speed < target && speed < 0){
                que.push({position, 1, steps + 1});
            }
            
            if(position + speed > target && speed > 0){
                que.push({position, -1, steps + 1});
            }
        }
        return ans;
    }
};
