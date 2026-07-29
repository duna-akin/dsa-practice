class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0

        if len(s) == 1:
            return 1

        for i in range(len(s)):
            currL = 1
            charSet = {s[i]}
            for j in range(i + 1, len(s)):
                if s[j] not in charSet:
                    currL += 1
                    charSet.add(s[j])
                else:
                    maxL = max(currL, maxL)
                    break
                maxL = max(currL, maxL)
        return maxL
