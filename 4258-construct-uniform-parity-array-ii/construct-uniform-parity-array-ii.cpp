class Solution {
public:
    bool uniformArray(vector<int>& nums1) {
        int xmin=INT_MAX , odd=0;

        for (int x: nums1){
            odd+=(x&1);
            xmin=min(xmin,x);
        }
        return xmin&1 || odd==0;
    }
};