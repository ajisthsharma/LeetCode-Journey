class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int summ=0,total=0;

        for(auto num: nums) total+=num;

        for(int i=0; i<nums.size(); i++){
            if (summ==total-summ-nums[i])
                return i;
            
            summ+=nums[i];
        }

        return -1;
    }
};