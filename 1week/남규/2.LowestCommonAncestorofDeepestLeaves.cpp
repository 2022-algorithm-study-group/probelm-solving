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
    int depth = -1;
    
    void dfs(TreeNode* node, int d){
        if(node->left){
            dfs(node->left, d + 1);
        }
        
        if(node->right){
            dfs(node->right, d + 1);
        }
        
        depth = max(d, depth);
    }
    
    TreeNode* answer(TreeNode* node, int d){
        if(d == depth){
            return node;
        }
        
        TreeNode* left = NULL;
        TreeNode* right = NULL;
        
        if(node->left){
            left = answer(node->left, d + 1);
        }
        
        if(node->right){
            right = answer(node->right, d + 1);
        }
        
        if(left && right){
            return node;
        }
        
        if(left && !right){
            return left;
        }
        
        if(!left && right){
            return right;
        }
        
        return NULL;
    }
    
    TreeNode* lcaDeepestLeaves(TreeNode* root) {
        if(!root){
            return NULL;
        }
        
        // Time Complexity: O(N)
        // Space Complexity: O(D), D: deepest depth of tree
        
        
        // deepest depth를 구한다.
        dfs(root, 0);
        
        // deepest depth에 도달한 경우 node 객체를 반환하여 lowest common ancestor를 구한다.
        return answer(root, 0);
    }
};
