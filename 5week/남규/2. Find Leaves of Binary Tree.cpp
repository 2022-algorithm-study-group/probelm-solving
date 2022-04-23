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
    bool removeLeafs(TreeNode* curr, vector<int>& leafs){
        if(!curr->left && !curr->right){
            leafs.push_back(curr->val);
            return true;
        }
        
        if(curr->left){
            bool isLeaf = removeLeafs(curr->left, leafs);
            if(isLeaf){
                curr->left = NULL;
            }
        }
        
        if(curr->right){
            bool isLeaf = removeLeafs(curr->right, leafs);
            if(isLeaf){
                curr->right = NULL;
            }
        }
        return false;
    }
    
    vector<vector<int>> findLeaves(TreeNode* root) {
        vector<vector<int>> ans;
        if(!root) return ans;
        
        while(root){
            if(!root->left && !root->right){
                ans.push_back({root->val});
                break;
            }
            
            vector<int> leafs;
            removeLeafs(root, leafs);
            ans.push_back(leafs);
        }
        return ans;
    }
};
