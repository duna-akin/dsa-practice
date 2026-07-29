class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, maxf, out, freqMap, = 0, 0, 0, dict()
        for r in range(len(s)):
            freqMap[s[r]] = freqMap.get(s[r], 0) + 1
            maxf = max(maxf, freqMap[s[r]])
            if ((r - l + 1) - maxf) > k:
                freqMap[s[l]] = freqMap[s[l]] - 1
                l += 1
            out = max(out, r - l + 1)
        return out