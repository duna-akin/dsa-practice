class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxF = 0
        longest_window = 0
        freqMap = dict()
        l = 0
        r = 0
        while r < len(s):
            freqMap[s[r]] = freqMap.get(s[r], 0) + 1
            maxF = max(maxF, freqMap[s[r]])
            if r - l + 1 - maxF > k:
                freqMap[s[l]] -= 1
                l += 1
            longest_window = max(longest_window, r - l + 1)
            r += 1
        return longest_window