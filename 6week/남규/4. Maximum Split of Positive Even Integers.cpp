class Solution {
public:
    vector<long long> maximumEvenSplit(long long finalSum) {
        vector<long long> ans;
        
        if(finalSum % 2 == 1) return ans;
        
        for(long long even = 2; finalSum; even += 2){
            if(even == finalSum){
                ans.push_back(even);
                break;
            }
            
            if(finalSum - even >= even + 2){
                finalSum -= even;
                ans.push_back(even);
            }
        }
        return ans;
    }
};
