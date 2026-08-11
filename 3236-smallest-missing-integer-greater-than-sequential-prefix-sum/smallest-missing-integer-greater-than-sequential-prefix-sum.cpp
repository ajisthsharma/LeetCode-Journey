class Solution {
public:
    int missingInteger(vector<int>& nums) {
        int pref=nums[0];
        
        for (int i=1; i<nums.size(); i++){
            if (nums[i]!=nums[i-1]+1)
                break;

            pref+=nums[i];
        }

        std::unordered_set<int> seen(nums.begin(), nums.end());

        while (seen.count(pref)) {
            pref++;
        }

        return pref;
    }
};