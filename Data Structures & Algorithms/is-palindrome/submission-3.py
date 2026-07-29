class Solution:
    def isPalindrome(self, s: str) -> bool:

        if len(s) == 1:
            return True

        s = s.lower()
        leftPI = 0
        rightPI = len(s) - 1

        while leftPI < rightPI:

            while leftPI < rightPI and not s[leftPI].isalnum():
                leftPI += 1

            while leftPI < rightPI and not s[rightPI].isalnum():
                rightPI -= 1

            if s[leftPI] != s[rightPI]:
                return False

            leftPI += 1
            rightPI -= 1


        return True