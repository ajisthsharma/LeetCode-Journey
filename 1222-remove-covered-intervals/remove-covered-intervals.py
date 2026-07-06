class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans=0
        a=b=-1

        for c,d in intervals:
            if c>a and d>b:
                a=c
                ans+=1

            b=max(b,d)

        return ans