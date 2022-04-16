// https://leetcode.com/problems/print-binary-tree/

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
class Solution {
public:
    int height = 0;
    
    void dfs(TreeNode* node, int depth){
        if(node->left){
            dfs(node->left, depth + 1);
        }
        
        if(node->right){
            dfs(node->right, depth + 1);
        }
        
        height = max(height, depth);
    }
    
    vector<vector<string>> printTree(TreeNode* root) {
        dfs(root, 0);
        int n = pow(2, height + 1) - 1;
        vector<vector<string>> matrix(height + 1, vector<string>(n, ""));
        
        unordered_map<TreeNode*, pair<int, int>> m;
        queue<TreeNode*> que;
        
        que.push(root);
        m[root] = {0, (n - 1) / 2};
        
        while(!que.empty()){
            TreeNode* curr = que.front();
            que.pop();
            
            int currY = m[curr].first;
            int currX = m[curr].second;
            int val = curr->val;
            bool isMinus = false;
            if(val < 0) {
                isMinus = true;
                val = -val;
            }
            
            if(val == 0){
                string cand = "0";
                matrix[currY][currX] = cand;
            } else {
                string cand = "";
                while(val){
                    string v = "";
                    v += ('0' + (val % 10));
                    cand = v + cand;
                    val /= 10;
                }
                matrix[currY][currX] = isMinus ? "-" + cand : cand;
            }
            
            if(curr->left){
                que.push(curr->left);
                m[curr->left] = {currY + 1, currX - pow(2, height - currY - 1)};
            }
            
            if(curr->right){
                que.push(curr->right);
                m[curr->right] = {currY + 1, currX + pow(2, height - currY - 1)};
            }
        }
        return matrix;
    }
};
