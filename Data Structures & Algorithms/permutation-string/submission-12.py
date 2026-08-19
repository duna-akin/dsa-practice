class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_count = [0] * 26
        win_count = [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            win_count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1_count[i] == win_count[i]:
                matches += 1
        
        if matches == 26: 
            return True
        
        l = 0 
        r = len(s1)
        while r < len(s2):
            r_code = ord(s2[r]) - ord('a')
            win_count[r_code] += 1
            if win_count[r_code] == s1_count[r_code]:
                matches += 1
            elif win_count[r_code] - 1 == s1_count[r_code]:
                matches -= 1
            
            l_code = ord(s2[l]) - ord('a')
            win_count[l_code] -= 1
            if win_count[l_code] == s1_count[l_code]:
                matches += 1
            elif win_count[l_code] + 1 == s1_count[l_code]:
                matches -= 1
            
            if matches == 26:
                return True
            
            l += 1
            r += 1
        return False
