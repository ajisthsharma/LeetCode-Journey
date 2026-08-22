class Solution:
    def minimumSteps(self, s: str) -> int:
        swap=black=0

        for ball in s:
            if ball=="0":
                swap+=black
            else:
                black+=1

        return swap