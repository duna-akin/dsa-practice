class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = dict()
        maxf = 0
        out = 0
        l, r = 0, 0

        while r < len(s):
            freqMap[s[r]] = freqMap.get(s[r], 0) + 1
            maxf = max(maxf, freqMap[s[r]])
            while r - l + 1 - maxf > k: # window size - max char freq has to be greater than our change budget
                freqMap[s[l]] -= 1
                l += 1
            out = max(out, r - l + 1)
            r += 1
        
        return out
