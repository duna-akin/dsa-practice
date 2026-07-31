class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # permutation is impossible if s2 is shorter than s1
        if len(s2) < len(s1):
            return False

        # store char frequencies as num encodings
        s1_freq, window_freq = [0] * 26, [0] * 26 

        # track how many frequencies match, if = 26 then it is a perm
        matches = 0

        # fill out the s1 and current window chars frequencies
        for i in range(len(s1)):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            window_freq[ord(s2[i]) - ord('a')] += 1
        
        # check matches for s1 and first s2 window char freqs
        for i in range(len(s1_freq)):
            if s1_freq[i] == window_freq[i]:
                matches += 1

        if matches == 26: 
            return True

        # sliding window solution

        l, r = 0, len(s1)
        while r < len(s2):
            # extract encoding of new char on right
            r_code = ord(s2[r]) - ord('a')

            # increment the new chars frequency
            window_freq[r_code] += 1

            # new freq match
            if window_freq[r_code] == s1_freq[r_code]:
                matches += 1
            
            # the chars frequency used to match, but doesn't anymore
            elif window_freq[r_code] - 1 == s1_freq[r_code]:
                matches -= 1
            
            # exact opposite condition but same logic for the old char on left
            l_code = ord(s2[l]) - ord('a')
            window_freq[l_code] -= 1
            if window_freq[l_code] == s1_freq[l_code]:
                matches += 1
            elif window_freq[l_code] + 1 == s1_freq[l_code]:
                matches -= 1

            if matches == 26: 
                return True
            
            # shift window right by one
            r += 1
            l += 1
        
        return False



