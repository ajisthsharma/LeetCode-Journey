class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        counts = Counter()
        result = []
        
        for num in nums:
            if counts[num]<k:
                result.append(num)
                counts[num]+=1
        return result