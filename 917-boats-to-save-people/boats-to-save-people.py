class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        st,end=0,len(people)-1
        ans=0

        while st<=end:
            if people[st]+people[end]<=limit:
                st+=1
            end-=1
            ans+=1

        return ans