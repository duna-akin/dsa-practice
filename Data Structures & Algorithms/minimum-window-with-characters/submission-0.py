class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = {}
        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)

        # inits
        winCount = {}
        have = 0
        need = len(tCount) # amount of distinct chars in t whose frequencies we need to match in the substring
        res = [-1, -1]
        resLen = float("inf")

        # sliding a dynamic-size window
        l = 0
        for r in range(len(s)):
            c = s[r]
            winCount[c] = 1 + winCount.get(c, 0)

            if c in tCount and winCount[c] == tCount[c]: # new match!
                have += 1
            
            # shrink from left
            # while window is valid (all characters alongside correct char freqs in t exists in the substring)
            while have == need:
                if resLen > r - l + 1:
                    res = [l, r]
                    resLen = r - l + 1
                
                winCount[s[l]] -= 1
                if s[l] in tCount and winCount[s[l]] < tCount[s[l]]: # lost a match :(
                    have -= 1
                l += 1

        return s[res[0]:res[1] + 1] if res != [-1, -1] else ""