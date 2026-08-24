class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        int pref_sum=0;
        std::unordered_map<int,int>sums;
        sums[0]=1;
        int ans=0;

        for (auto num : nums){
            pref_sum+=num;
            int key=pref_sum%k;

            if (key<0) key+=k;

            if (sums.find(key)!=sums.end()){
                ans+=sums[key];
                sums[key]+=1;
                continue;
            }
            sums[key]=1;
        }

        return ans;
    }
};