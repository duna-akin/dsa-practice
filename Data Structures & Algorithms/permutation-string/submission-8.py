class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # permutation: same length, same chars, same char frequencies
        # hence we look at windows within s2 that are the size of s1

        if len(s2) < len(s1):
            return False

        # chars encoded as indices a-z: 0-25 with values indicating freq
        s1_freq = [0] * 26
        window_freq = [0] * 26

        # how many freqs match, aiming for 26 (for each char)
        matches = 0

        # find the char freqs of s1 and the first window in s2
        for i in range(len(s1)):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            window_freq[ord(s2[i]) - ord('a')] += 1

        # check how many matches are there currently
        for i in range(26):
            if s1_freq[i] == window_freq[i]:
                matches += 1
        
        # return immediately if all match
        if matches == 26: return True

        # edges of window
        l, r = 0, len(s1)

        while r < len(s2):
            # extract the code of new char from right
            r_code = ord(s2[r]) - ord('a')

            # increment the new chars freq
            window_freq[r_code] += 1

            if window_freq[r_code] == s1_freq[r_code]:
                matches += 1
            elif window_freq[r_code] - 1 == s1_freq[r_code]: # used to match, now doesn't
                matches -= 1
            
            # extract the code of old char from left
            l_code = ord(s2[l]) - ord('a')

            # decrement the old chars freq
            window_freq[l_code] -= 1

            if window_freq[l_code] == s1_freq[l_code]:
                matches += 1
            elif window_freq[l_code] + 1 == s1_freq[l_code]: # used to match, now doesn't
                matches -= 1

            l += 1
            r += 1
            if matches == 26:
                return True
        return False
