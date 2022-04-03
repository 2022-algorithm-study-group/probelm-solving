/*
// Definition for Employee.
class Employee {
public:
    int id;
    int importance;
    vector<int> subordinates;
};
*/

class Solution {
public:
    int getImportance(vector<Employee*> employees, int id) {
        stack<int> stk;
        stk.push(id);
        int ans = 0;
        
        // Time Complexity: O(N)
        // Space Complexity: O(N)
        unordered_map<int, Employee*> idToEmp;
        
        for(auto employee : employees){
            idToEmp[employee->id] = employee;
        }
        
        // unordered_set<int> visited;
        
        while(!stk.empty()){
            int curr = stk.top();
            ans += idToEmp[curr]->importance;
            stk.pop();
            
            for(int i = 0; i < idToEmp[curr]->subordinates.size(); i++){
                int next = idToEmp[curr]->subordinates[i];
                /*if(visited.find(next) != visited.end()) continue;
                visited.insert(next);*/
                stk.push(next);
            }
        }
        return ans;
    }
};
