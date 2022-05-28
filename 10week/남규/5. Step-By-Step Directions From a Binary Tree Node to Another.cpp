/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

/*
TC1
root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"

TC2
root = [2,1], startValue = 2, destValue = 1
Output: "L"

Approach
1. from root to both startValue and destValue string path using DFS
1.1 from root to startValue: LL -> s
1.2 from root to destValue: RL -> d

2. skip all values from index 0 to i if s[i] == d[i]; -> LCA

3. ans = string('U', s.size()) + d;

Time Complexity: O(N), N: the number of all nodes in a binary tree
Space Complexity: O(2N) = O(N)
*/

class Solution {
public:
    string s = "";
    string d = "";
    int startValue;
    int destValue;
    
    void findTreePath(TreeNode* curr, string& path){
        if(s != "" && d != ""){
            return;
        }
        
        if(curr->val == startValue){
            this->s = path;
        }
        
        if(curr->val == destValue){
            this->d = path;
        }
        
        if(curr->left){
            path.push_back('L');
            findTreePath(curr->left, path);
            path.pop_back();
        }
        
        if(curr->right){
            path.push_back('R');
            findTreePath(curr->right, path);
            path.pop_back();
        }
    }
    
    string getDirections(TreeNode* root, int startValue, int destValue) {
        if(!root){
            return "";
        }
        
        this->startValue = startValue;
        this->destValue = destValue;
        string path = "";
        findTreePath(root, path);
        
        // s = "";
        // d = "L"
        
        // s and d are valid
        int base = 0;
        for(int i = 0; i < min(s.size(), d.size()); i++){
            if(s[i] == d[i]){
                base = i + 1;
            } else {
                break;
            }
        }
        
        // TC1
        // UU + RL => UURL
        
        // TC2
        
        // cout << s << "\n" << d << "\n" << base << endl;
        
        return string(s.size() - base, 'U') + d.substr(base);
    }
};
