class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # a window is valid iff [window size - frequency of most occurring char] <= k
        # dynamic window size that either increases or stays the same
        l, r = 0, 0
        out = 0
        maxf = 0 # frequency of most occurring char
        freqMap = dict() # store each char's freq here

        while r < len(s):
            freqMap[s[r]] = freqMap.get(s[r], 0) + 1
            maxf = max(maxf, freqMap[s[r]])
            if r - l + 1 - maxf > k:
                freqMap[s[l]] -= 1
                l += 1
            out = max(out, r - l + 1)
            r += 1
        return out # the length of the longest window that first the condition

