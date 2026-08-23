class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2

        s1 = sum(int(c) for c in num[:mid] if c != "?")
        s2 = sum(int(c) for c in num[mid:] if c != "?")

        q1 = num[:mid].count("?")
        q2 = num[mid:].count("?")

        return (s1 - s2) * 2 != (q2 - q1) * 9