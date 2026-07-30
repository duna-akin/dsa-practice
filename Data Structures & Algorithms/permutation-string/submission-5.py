class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_freq, window_freq = [0] * 26, [0] * 26 # array for chars 0-25 (a-z)
        matches = 0
        l, r = 0, len(s1)

        for i in range(len(s1)):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            window_freq[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            if s1_freq[i] == window_freq[i]:
                matches += 1
        
        if matches == 26:
            return True
        
        while r < len(s2):
            r_code = ord(s2[r]) - ord('a')
            window_freq[r_code] += 1
            if window_freq[r_code] == s1_freq[r_code]:
                matches += 1
            elif window_freq[r_code] - 1 == s1_freq[r_code]:
                matches -= 1

            l_code = ord(s2[l]) - ord('a')
            window_freq[l_code] -= 1
            if window_freq[l_code] == s1_freq[l_code]:
                matches += 1
            elif window_freq[l_code] + 1 == s1_freq[l_code]:
                matches -= 1
            
            l += 1
            r += 1
            if matches == 26:
                return True
        return False

