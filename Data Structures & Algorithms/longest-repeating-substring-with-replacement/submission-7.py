class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = dict()
        maxf = 0
        output = 0
        l, r = 0, 0

        while r < len(s):
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1
            maxf = max(maxf, freq_map[s[r]])
            while r - l + 1 - maxf > k:
                freq_map[s[l]] -= 1
                l += 1
            output = max(maxf, r - l + 1)
            r += 1
        
        return output
