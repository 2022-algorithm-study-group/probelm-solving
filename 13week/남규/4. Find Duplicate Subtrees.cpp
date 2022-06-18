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
    unordered_map<string, int> dups;
    vector<TreeNode*> ans;
    
    string inorder(TreeNode* node){
        string ret = to_string(node->val);
        
        string leftv = ",";
        if(node->left){
            leftv += inorder(node->left);
        }
        ret += leftv;
        
        string rightv = ",";
        if(node->right){
            rightv += inorder(node->right);
        }
        ret += rightv;
        
        if(dups[ret] == 1){
            ans.push_back(node);
            dups[ret]++;
        } else {
            dups[ret]++;
        }
        return ret;
    }
    
    vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        inorder(root);
        return ans;
    }
};
