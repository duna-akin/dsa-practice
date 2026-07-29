class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1

        while left < right:

            # skip non alphanumeric chars
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            # check
            if s[left].lower() != s[right].lower():
                return False

            # move indices after passing check
            left += 1
            right -= 1

        return True
