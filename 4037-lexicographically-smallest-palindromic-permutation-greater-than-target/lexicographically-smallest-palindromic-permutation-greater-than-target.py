class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        m = n // 2

        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
            
        odd_char = ""
        half_count = [0] * 26
        for i in range(26):
            if freq[i] % 2 != 0:
                if odd_char != "":
                    return ""
                odd_char = chr(ord('a') + i)
            half_count[i] = freq[i] // 2
            
        if n % 2 == 0 and odd_char != "":
            return ""

        exact_match = True
        temp_half = list(half_count)
        prefix_chars = []
        
        for i in range(m):
            idx = ord(target[i]) - ord('a')
            if temp_half[idx] > 0:
                temp_half[idx] -= 1
                prefix_chars.append(target[i])
            else:
                exact_match = False
                break
                
        if exact_match:
            first_half = target[:m]
            full_pal = first_half + odd_char + first_half[::-1]
            if full_pal > target:
                return full_pal

        curr_half = list(half_count)
        matched_len = 0
        while matched_len < m:
            idx = ord(target[matched_len]) - ord('a')
            if curr_half[idx] > 0:
                curr_half[idx] -= 1
                matched_len += 1
            else:
                break
                
        for i in range(matched_len, -1, -1):
            if i < m:
                target_idx = ord(target[i]) - ord('a')

                for c in range(target_idx + 1, 26):
                    if curr_half[c] > 0:
                        curr_half[c] -= 1

                        suffix_half = []
                        for ch_idx in range(26):
                            if curr_half[ch_idx] > 0:
                                suffix_half.append(chr(ord('a') + ch_idx) * curr_half[ch_idx])
                                
                        first_half = target[:i] + chr(ord('a') + c) + "".join(suffix_half)
                        return first_half + odd_char + first_half[::-1]

            if i > 0:
                curr_half[ord(target[i - 1]) - ord('a')] += 1
                
        return ""