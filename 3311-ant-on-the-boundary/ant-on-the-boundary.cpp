class Solution {
public:
    int returnToBoundaryCount(vector<int>& nums) {
        int ans=0,summ=0;

        for(int num: nums){
            summ+=num;

            if (summ==0) ans+=1;
        }
        return ans;
    }
};