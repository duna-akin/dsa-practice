class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        winCount = [0] * 26
        s1Count = [0] * 26
        matches = 0

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            winCount[ord(s2[i]) - ord('a')] += 1
        
        for i in range(26):
            if s1Count[i] == winCount[i]:
                matches += 1
        
        if matches == 26:
            return True
        
        l = 0
        r = len(s1)

        while r < len(s2):
            r_code = ord(s2[r]) - ord('a')
            winCount[r_code] += 1

            if winCount[r_code] == s1Count[r_code]:
                matches += 1
            elif winCount[r_code] - 1 == s1Count[r_code]:
                matches -= 1
            
            l_code = ord(s2[l]) - ord('a')
            winCount[l_code] -= 1

            if winCount[l_code] == s1Count[l_code]:
                matches += 1
            elif winCount[l_code] + 1 == s1Count[l_code]:
                matches -= 1
            
            l += 1
            r += 1
            if matches == 26:
                return True
        return False
