class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = {}
        fMax = 0
        res = 0

        # slide a dynamic-size window
        l = 0
        for r in range(len(s)):
            c = s[r]
            freqMap[c] = 1 + freqMap.get(c, 0)
            fMax = max(fMax, freqMap[c])

            # shrink window while it is invalid
            while r - l + 1 - fMax > k:
                freqMap[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res