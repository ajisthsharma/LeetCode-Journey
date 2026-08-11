class Solution {
public:
    int solve(vector<int>& potions,long long strength,long long success){
        int low=0,high=potions.size()-1;
        int idx=-1;

        while (low<=high){
            int mid=low+(high-low)/2;

            if (potions[mid]*strength>=success){
                high=mid-1;
                idx=mid;
            }
            else
                low=mid+1;
            }

        return idx;
    }

    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        sort(potions.begin(),potions.end());
        std::vector<int> ans(spells.size());

        for (int i=0; i<spells.size(); i++){
            int idx=solve(potions,spells[i],success);
            if (idx!=-1) ans[i]=potions.size()-idx;
        }

        return ans;
    }
};