class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        current = 0
        for i in range(k):
            if s[i] in vowels:
                current += 1
        max = current
        for i in range(k, len(s)):
            if s[i] in vowels:
                current += 1
            if s[i - k] in vowels:
                current -= 1
            if current > max:
                max = current
        return max