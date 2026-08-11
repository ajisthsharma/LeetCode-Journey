class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        L, R = 0, len(height) - 1
        LeftMax, RightMax =0, 0
        
        while L < R:
            if height[L] < height[R]:
                LeftMax = max(LeftMax, height[L])
                water += LeftMax - height[L]
                L+=1
            else:
                RightMax = max(RightMax, height[R])
                water += RightMax - height[R]
                R-=1
        return water

 
        