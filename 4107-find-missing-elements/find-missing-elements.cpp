class Solution {
public:
    vector<int> findMissingElements(vector<int>& nums) {
        int mini = *min_element(nums.begin(),nums.end());

        int maxi = *max_element(nums.begin(),nums.end());

        sort(nums.begin(),nums.end());

        vector<int> ans;
        int l = 0;

        for(int i = mini;i <= maxi;i++){
            if(nums[l] != i){
                ans.push_back(i);
            }else{
                l++;
            }
        }

        return ans;
    }
};