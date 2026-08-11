class Solution {
public:
    int trap(vector<int>& height) {
        int water = 0;
        int L = 0, R= height.size() - 1;
        int LeftMax=0,RightMax=0;
        
        while (L < R){
            if (height[L] < height[R]){
                LeftMax = max(LeftMax, height[L]);
                water += LeftMax - height[L];
                L+=1;
            }
            else{
                RightMax = max(RightMax, height[R]);
                water += RightMax - height[R];
                R-=1;
            }
        }
        return water;
    }
};