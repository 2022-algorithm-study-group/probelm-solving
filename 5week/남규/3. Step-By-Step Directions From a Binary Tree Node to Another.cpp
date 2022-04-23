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
    void traverse(TreeNode* curr, string& s, int v1, int v2, string &start, string &end){
        if(curr->left){
            s.push_back('L');
            traverse(curr->left, s, v1, v2, start, end);
            s.pop_back();
        }
        
        if(curr->right){
            s.push_back('R');
            traverse(curr->right, s, v1, v2, start, end);
            s.pop_back();
        }
        
        if(v1 == curr->val){
            start = s;
            return;
        }
        
        if(v2 == curr->val){
            end = s;
            return;
        }
    }
    
    string getDirections(TreeNode* root, int startValue, int destValue) {
        string s = "";
        string e = "";
        string tmp = "";
        traverse(root, tmp, startValue, destValue, s, e);
        int lca = 0;
        for(; lca < min(s.size(), e.size()); lca++){
            if(s[lca] != e[lca]){
                break;
            }
        }
        return string(s.size() - lca, 'U')  + e.substr(lca);
    }
};
