class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)): # i: start of substring
            freqMap = dict()
            maxf = 0
            for j in range(i, len(s)): # j: end of substring
                freqMap[s[j]] = freqMap.get(s[j], 0) + 1
                maxf = max(maxf, freqMap[s[j]])
                if (j - i + 1) - maxf <= k:
                    res = max(res, j - i + 1)
        
        return res