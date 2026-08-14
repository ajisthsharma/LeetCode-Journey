class Solution {
public:
    int curr = 0;
    TreeNode* convertBST(TreeNode* root) {
        if(!root) return nullptr;
        root->right = convertBST(root->right);
        curr += root->val;
        root->val = curr;
        root->left = convertBST(root->left);
        return root;
    }
};