class Solution {
public:
    int oddEvenJumps(vector<int>& arr) {
        // Ex1) 2, 6, 4, 3, 5
        // 3
        // edge cases
        // length = 1
        
        // Ex2) 5
        // 1
        
        // Ex3) 2, 6, 4, 3, 3, 3, 5
        
        // Odd jump
        // Even jump
        
        // Time complexity: O(N log N)
        // Space complexity: O(N)
        
        int n = arr.size();
        
        vector<bool> odd(n, false);
        vector<bool> even(n, false);
        odd[n - 1] = even[n - 1] = true;
        
        map<int, int> valueToIndex;
        valueToIndex[arr[n - 1]] = n - 1;
        
        for(int i = n - 2; i >= 0; i--){
            int curr = arr[i];
            
            if(valueToIndex.find(curr) == valueToIndex.end()){
                // A odd-numbered jump
                auto lo = valueToIndex.lower_bound(curr);
                if(lo != valueToIndex.end()){
                    int index = lo->second;
                    odd[i] = even[index];
                }
                
                // A even-numbered jump
                // Ex3) 2, 6, 4, map: (3, 3, 3, 5)
                auto hi = valueToIndex.upper_bound(curr);
                if(hi != valueToIndex.begin()){
                    hi--;
                    int index = hi->second;
                    even[i] = odd[index];
                }
            } else {
                int index = valueToIndex[curr];
                odd[i] = even[index];
                even[i] = odd[index];
            }
            valueToIndex[curr] = i;
        }
        
        int ans = 0;
        for(int i = 0; i < n; i++){
            ans += odd[i];
        }
        return ans;
    }
};
