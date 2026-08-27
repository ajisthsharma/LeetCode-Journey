class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        matched_len = 0
        while matched_len < n:
            idx = ord(target[matched_len]) - ord('a')
            if count[idx] > 0:
                count[idx] -= 1
                matched_len += 1
            else:
                break

        for i in range(matched_len, -1, -1):
            if i < n:
                target_char_idx = ord(target[i]) - ord('a')

                for c in range(target_char_idx + 1, 26):
                    if count[c] > 0:
                    
                        count[c] -= 1

                        suffix = []
                        for ch_idx in range(26):
                            if count[ch_idx] > 0:
                                suffix.append(chr(ord('a') + ch_idx) * count[ch_idx])
                                
                        return target[:i] + chr(ord('a') + c) + "".join(suffix)

            if i > 0:
                count[ord(target[i - 1]) - ord('a')] += 1
                
        return ""