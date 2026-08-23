class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = {}
        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)
        
        winCount = {}
        have = 0
        need = len(tCount)
        res = [-1, -1]
        resLen = float("inf")

        l = 0
        for r in range(len(s)):
            c = s[r]
            winCount[c] = 1 + winCount.get(c, 0)

            if c in tCount and winCount[c] == tCount[c]:
                have += 1

            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                winCount[s[l]] -= 1
                if s[l] in tCount and winCount[s[l]] < tCount[s[l]]:
                    have -= 1
                
                l += 1
        
        return s[res[0]:res[1] + 1] if res != [-1, -1] else ""