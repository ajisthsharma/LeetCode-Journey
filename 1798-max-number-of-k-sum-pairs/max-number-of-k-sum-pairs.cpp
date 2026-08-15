class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end());
        int i=0,j=nums.size()-1;
        int ans=0;

        while (i<j){
            int summ=nums[i]+nums[j];

            if (summ==k){
                ans+=1;
                i+=1;
                j-=1;
            }

            else if (summ>k)
                j-=1;

            else
                i+=1;
        }

        return ans;
    }
};