class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = ceil(sum(piles)/h)

        low, high = k,max(piles)
        
        while low<high:
            taken = 0

            for pile in piles:
                taken +=ceil(pile/k)

            if taken <= h:
                high = k
            else:
                low = k+1 

            k = (low+high)//2

        return k

        